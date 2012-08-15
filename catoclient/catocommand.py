#########################################################################
# Copyright 2011 Cloud Sidekick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#########################################################################

# This file is a derived work from Eucalyptus 
# euca2ools/euca2ools/commands/eucacommands.py
# released under the BSD license
# original copyright: 
#        (c) 2009-2011, Eucalyptus Systems, Inc.`
# original authors:
#       Neil Soman neil@eucalyptus.com
#       Mitch Garnaat mgarnaat@eucalyptus.com

import getopt
import os
import sys
import textwrap
import urlparse
import hashlib
import base64
import hmac
import urllib
import urllib2
import json
from datetime import datetime
from catoclient.param import Param

try:
    import xml.etree.cElementTree as ET
except (AttributeError, ImportError):
    import xml.etree.ElementTree as ET
try:
    ET.ElementTree.iterfind
except AttributeError as ex:
    del(ET)
    import catoxml.etree.ElementTree as ET


class CatoCommand(object):

    Description = 'Base class'
    StandardOptions = [
                       Param(name='access_key',
                             short_name='a', long_name='access-key',
                             doc="User's Access Key ID.",
                             optional=True),
                       Param(name='secret_key',
                             short_name='s', long_name='secret-key',
                             doc="User's Secret Key.",
                             optional=True),
                       Param(name='config_file',
                             short_name=None, long_name='config',
                             doc="""Read credentials from the specified config file.""",
                             optional=True),
                       Param(name='output_format', short_name=None, long_name='format',
                             doc='The output format.  (default=text, values=xml/json.)',
                             optional=True, ptype='string', choices=['text', 'json', 'xml']),
                       Param(short_name=None, long_name='debug',
                             doc='Turn on debugging output.',
                             optional=True, ptype='boolean'),
                       Param(short_name='h', long_name='help',
                             doc='Display this help message.',
                             optional=True, ptype='boolean'),
                       Param(short_name='U', long_name='url',
                             doc='URL of the Cloud to connect to.',
                             optional=True),
                       Param(short_name=None, long_name='version',
                             doc='Display the version of this tool.',
                             optional=True, ptype='boolean')
                       ]
    Options = []
    Args = []

    def __init__(self, debug=False):
        self.access_key_short_name = '-a'
        self.secret_key_short_name = '-s'
        self.access_key = None
        self.secret_key = None
        self.url = None
        self.config_file_name = None
        self.debug = 0
        self.set_debug(debug)
        self.cmd_name = os.path.basename(sys.argv[0])
        self.process_cli_args()
        
        # if there's a config file, we read it.
        # any required values not explicitly specified on the command line,
        # are read from the config file.
        # there's a default file ".catoclient.conf", and you can override with the "config_file" argument
        configargs = None
        cfn = None
        if self.config_file_name:
            cfn = self.config_file_name
        else:
            cfn = "catoclient.conf"
        
        try:
            with open(cfn, 'r') as f_in:
                if f_in:
                    configargs = json.loads(f_in.read())
        except ValueError as ex:
            # if a name was explicitly specified and is bad, bark... 
            # if it's the default file and missing, don't complain
            if cfn != "catoclient.conf":
                print("The specified config file (%s) doesn't exist or the json format is invalid." % self.config_file_name)
                self.error_exit()
 
        if configargs:
            # loop through the settings
            for k, v in configargs.items():
                setattr(self, k, v)

    def set_debug(self, debug=False):
        if debug:
            self.debug = 2

    def process_cli_args(self):
        try:
            (opts, args) = getopt.gnu_getopt(sys.argv[1:],
                                             self.short_options(),
                                             self.long_options())
        except getopt.GetoptError, e:
            print(e)
            sys.exit(1)
        for (name, value) in opts:
            if name in ('-h', '--help'):
                self.usage()
                sys.exit()
            elif name == '--version':
                self.version()
            elif name == '--debug':
                self.set_debug(True)
            elif name in (self.access_key_short_name, '--access-key'):
                self.access_key = value
            elif name in (self.secret_key_short_name, '--secret-key'):
                self.secret_key = value
            elif name in ('-U', '--url'):
                self.url = value
            elif name == '--config':
                self.config_file_name = value
            else:
                option = self.find_option(name)
                if option:
                    try:
                        value = option.convert(value)
                    except:
                        msg = '%s should be of type %s' % (option.long_name,
                                                           option.ptype)
                        self.display_error_and_exit(msg)
                    if option.choices:
                        if value not in option.choices:
                            msg = '%s value must be one of: %s' % (option.long_name, '|'.join(option.choices))
                            self.display_error_and_exit(msg)
                    if option.cardinality in ('*', '+'):
                        if not hasattr(self, option.name):
                            setattr(self, option.name, [])
                        getattr(self, option.name).append(value)
                    else:
                        setattr(self, option.name, value)
        self.handle_defaults()
        self.check_required_options()

        for arg in self.Args:
            if not arg.optional and len(args) == 0:
                self.usage()
                msg = 'Argument (%s) was not provided' % arg.name
                self.display_error_and_exit(msg)
            if arg.cardinality in ('*', '+'):
                setattr(self, arg.name, args)
            elif arg.cardinality == 1:
                if len(args) == 0 and arg.optional:
                    continue
                try:
                    value = arg.convert(args[0])
                except:
                    msg = '%s should be of type %s' % (arg.name,
                                                       arg.ptype)
                setattr(self, arg.name, value)
                if len(args) > 1:
                    msg = 'Only 1 argument (%s) permitted' % arg.name
                    self.display_error_and_exit(msg)

    def check_for_conflict(self):
        for option in self.Options:
            if option.short_name == 'a' or option.short_name == 's':
                self.access_key_short_name = '-A'
                self.secret_key_short_name = '-S'
                opt = self.find_option('--access-key')
                opt.short_name = 'A'
                opt = self.find_option('--secret-key')
                opt.short_name = 'S'

    def find_option(self, op_name):
        for option in self.StandardOptions + self.Options:
            if option.synopsis_short_name == op_name or option.synopsis_long_name == op_name:
                return option
        return None

    def short_options(self):
        s = ''
        for option in self.StandardOptions + self.Options:
            if option.short_name:
                s += option.getopt_short_name
        return s

    def long_options(self):
        l = []
        for option in self.StandardOptions + self.Options:
            if option.long_name:
                l.append(option.getopt_long_name)
        return l

    def required(self):
        return [ opt for opt in self.StandardOptions + self.Options if not opt.optional ]

    def required_args(self):
        return [ arg for arg in self.Args if not arg.optional ]

    def optional(self):
        return [ opt for opt in self.StandardOptions + self.Options if opt.optional ]

    def optional_args(self):
        return [ arg for arg in self.Args if arg.optional ]

    def handle_defaults(self):
        for option in self.Options + self.Args:
            if not hasattr(self, option.name):
                value = option.default
                if value is None and option.cardinality in ('+', '*'):
                    value = []
                elif value is None and option.ptype == 'boolean':
                    value = False
                elif value is None and option.ptype == 'integer':
                    value = 0
                setattr(self, option.name, value)

    def check_required_options(self):
        missing = []
        for option in self.required():
            if not hasattr(self, option.name) or getattr(self, option.name) is None:
                missing.append(option.long_name)
        if missing:
            msg = 'These required options are missing: %s' % ','.join(missing)
            self.display_error_and_exit(msg)

    def version(self):
        print('.01')
        sys.exit(0)

    def param_usage(self, plist, label, n=30):
        nn = 80 - n - 4
        if plist:
            print('\n%s' % label)
            for opt in plist:
                names = []
                if opt.short_name:
                    names.append(opt.synopsis_short_name)
                if opt.long_name:
                    names.append(opt.synopsis_long_name)
                if not names:
                    names.append(opt.name)
                doc = textwrap.dedent(opt.doc)
                doclines = textwrap.wrap(doc, nn)
                if opt.choices:
                    vv = 'Valid Values: %s' % '|'.join(opt.choices)
                    doclines += textwrap.wrap(vv, nn)
                if doclines:
                    print('    %s%s' % (','.join(names).ljust(n), doclines[0]))
                    for line in doclines[1:]:
                        print('%s%s' % (' ' * (n + 4), line))

    def option_synopsis(self, options):
        s = ''
        for option in options:
            names = []
            if option.short_name:
                names.append(option.synopsis_short_name)
            if option.long_name:
                names.append(option.synopsis_long_name)
            if option.optional:
                s += '['
            s += ', '.join(names)
            if option.ptype != 'boolean':
                if option.metavar:
                    n = option.metavar
                elif option.name:
                    n = option.name
                else:
                    n = option.long_name
                s += ' <%s> ' % n
            if option.optional:
                s += ']'
        return s

    def synopsis(self):
        s = '%s ' % self.cmd_name
        n = len(s) + 1
        t = ''
        t += self.option_synopsis(self.required())
        t += self.option_synopsis(self.optional())
        if self.Args:
            t += ' '
            arg_names = []
            for arg in self.Args:
                name = arg.name
                if arg.optional:
                    name = '[ %s ]' % name
                arg_names.append(name)
            t += ' '.join(arg_names)
        lines = textwrap.wrap(t, 80 - n)
        print s, lines[0]
        for line in lines[1:]:
            print '%s%s' % (' ' * n, line)
                
    def usage(self):
        print '%s\n' % self.Description
        self.synopsis()
        self.param_usage(self.required() + self.required_args(),
                         'REQUIRED PARAMETERS')
        self.param_usage(self.optional() + self.optional_args(),
                         'OPTIONAL PARAMETERS')

    def display_error_and_exit(self, exc):
        try:
            print '%s: %s' % (exc.error_code, exc.error_message)
        except:
            print '%s' % exc
        finally:
            sys.exit(1)

    def error_exit(self):
        sys.exit(1)

    def http_get(self, url, timeout=10):
        try:
            if not url:
                return "URL not provided."

            if self.debug:
                print "Trying an HTTP GET to %s" % url

            # for now, just use the url directly
            try:
                response = urllib2.urlopen(url, None, timeout)
                result = response.read()
                if result:
                    return result

            except urllib2.URLError as ex:
                if hasattr(ex, "reason"):
                    print "HTTPGet: failed to reach a server."
                    print ex.reason
                    return ex.reason
                elif hasattr(ex, "code"):
                    print "HTTPGet: The server couldn\'t fulfill the request."
                    print ex.__str__()
                    return ex.__str__()

            # if all was well, we won't get here.
            return "No results from request."

        except Exception as ex:
            raise ex

    def call_api(self, method, parameters):
        host = self.url
        key = self.access_key
        pw = self.secret_key
        outfmt = "text"
        # was a different output format specified?
        # we limit the values to xml or json.
        if hasattr(self, "output_format"):
            x = getattr(self, "output_format")
            if x:
                if x == "xml" or x == "json":
                    outfmt = x

        
        args = {}
        for param in parameters:
            #if hasattr(self, param):
            if getattr(self, param):
                args[param] = getattr(self, param)

        if len(args):
            arglst = ["&%s=%s" % (k, urllib.quote_plus(v)) for k, v in args.items()]
            argstr = "".join(arglst)
        else:
            argstr = ""

        #timestamp
        ts = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
        ts = ts.replace(":", "%3A")

        #string to sign
        string_to_sign = "{0}?key={1}&timestamp={2}".format(method, key, ts)

        #encoded signature
        sig = base64.b64encode(hmac.new(str(pw), msg=string_to_sign, digestmod=hashlib.sha256).digest())
        sig = "&signature=" + urllib.quote_plus(sig)

        of = "&output_format=%s" % outfmt
        url = "%s/%s%s%s%s" % (host, string_to_sign, sig, argstr, of)
        
        response = self.http_get(url)
        if self.debug:
            print(response)
            
        if response:
            if outfmt == "json":
                try:
                    d = json.loads(response)
                    if d["ErrorCode"]:
                        code = d["ErrorCode"]
                        detail = d["ErrorDetail"]
                        message = d["ErrorMessage"]
                        if detail:
                            msg = "%s, %s, %s" % (code, message, detail)
                        self.display_error_and_exit(msg)
                    else:
                        return d["Response"]
                except ValueError:
                    print("Response JSON could not be parsed.")
                    return response
                except Exception as ex:
                    raise ex
            elif outfmt == "xml":
                try:
                    xRoot = ET.fromstring(response)
                    if xRoot.findtext("error/code", None):
                        code = xRoot.findtext("error/code", "")
                        detail = xRoot.findtext("error/detail", "")
                        message = xRoot.findtext("error/message", "")

                        msg = "%s, %s, %s" % (code, detail, message)
                        self.display_error_and_exit(msg)
                    else:
                        innercontent = list(xRoot.find("response"))[0]
                        return ET.tostring(innercontent)
                except ValueError:
                    print("Response XML could not be parsed.")
                except Exception as ex:
                    raise ex
            else:
                return response
                
    def get_relative_filename(self, filename):
        return os.path.split(filename)[-1]

    def get_file_path(self, filename):
        # relative_filename = self.get_relative_filename(filename)
        file_path = os.path.dirname(filename)
        if len(file_path) == 0:
            file_path = '.'
        return file_path
