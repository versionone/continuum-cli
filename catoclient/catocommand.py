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
import httplib
import json
from urlparse import urlparse
from datetime import datetime
from catoclient.param import Param

try:
    import xml.etree.cElementTree as ET
except (AttributeError, ImportError):
    import xml.etree.ElementTree as ET


class CatoCommand(object):

    Description = ''
    API = ''
    Examples = ''
    Info = ''
    StandardOptions = [
                       Param(name='access_key',
                             short_name='A', long_name='access-key',
                             doc="A Cato user account username.",
                             optional=True),
                       Param(name='secret_key',
                             short_name='S', long_name='secret-key',
                             doc="A valid Cato user's password.",
                             optional=True),
                       Param(name='config_file',
                             short_name='C', long_name='config',
                             doc="""Read credentials and URL from the specified json formatted config file. If a config file and 
                                    -A, -U or -S flags are used on the same command, the flag option parameters take precendence""",
                             optional=True),
                       Param(name='output_format', short_name='F', long_name='format',
                             doc='The output format.  (default=text, values=xml/json.)',
                             optional=True, ptype='string', choices=['text', 'json', 'xml']),
                       Param(name='output_delimiter', short_name='L', long_name='output_delimiter',
                             doc='Delimiter for "Text" output format. (Default is TAB)',
                             optional=True, ptype='string'),
                       Param(name='debug', short_name='D', long_name='debug',
                             doc='Turn on debugging output.',
                             optional=True, ptype='boolean'),
                       Param(name='help', short_name='H', long_name='help',
                             doc='Display this help message.',
                             optional=True, ptype='boolean'),
                       Param(name='url', short_name='U', long_name='url',
                             doc='URL of the Cato webservice API endpoint. E.g.: http://address:port',
                             optional=True),
                       Param(name='force', long_name='force',
                             doc='Force "yes" on "Are you sure?" prompts.',
                             optional=True, ptype='boolean'),
                       Param(name='noheader', long_name='noheader',
                             doc='For "text" output format, omit the column header.',
                             optional=True, ptype='boolean'),
                       Param(name='dumpdoc', long_name='dumpdoc',
                             doc='Writes documentation for the command in Markdown format.',
                             optional=True, ptype='boolean'),
                       Param(name='api', long_name='api',
                             doc='Identifies the API endpoint associated with this command.',
                             optional=True, ptype='boolean')
                       ]
    Options = []
    Args = []

    def __init__(self, debug=False):
        self.access_key = None
        self.secret_key = None
        self.url = None
        self.config_file_name = None
        self.debug = 0
        self.force = False
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
            cfn = "%s/.catoclient.conf" % os.path.expanduser("~")
        
        try:
            with open(cfn, 'r') as f_in:
                if f_in:
                    configargs = json.loads(f_in.read())
        except IOError:
            # if the file doesn't exist, warn and exit (but continue if there's no default config file).
            if cfn != "%s/.catoclient.conf" % os.path.expanduser("~"):
                print("The specified config file (%s) could not be found." % cfn)
                self.error_exit()
            else:
                if self.debug:
                    print("The default config file (%s) could not be found." % cfn)
                    
        except ValueError:
            # if the format of either file is bad, bark about it
            print("The specified config file (%s) json format is invalid." % cfn)
            self.error_exit()
 
        if configargs:
            # loop through the settings
            for k, v in configargs.items():
                if hasattr(self, k):
                    if not getattr(self, k):
                        setattr(self, k, v)
                        
        # since the args can come from different sources, we have to explicitly check the required ones.
        if not self.url:
            print("URL is required, either via --url or in a config file.")
            self.error_exit()
        if not self.access_key:
            print("Access Key is required, either via --access-key or in a config file.")
            self.error_exit()
        if not self.secret_key:
            print("Secret Key is required, either via --secret-key or in a config file.")
            self.error_exit()

    def set_debug(self, debug=False):
        if debug:
            self.debug = 2

    def set_force(self, force=True):
        if force:
            self.force = True

    def process_cli_args(self):
        try:
            (opts, args) = getopt.gnu_getopt(sys.argv[1:],
                                             self.short_options(),
                                             self.long_options())
        except getopt.GetoptError, e:
            print(e)
            sys.exit(1)
        for (name, value) in opts:
            if name in ('-H', '--help'):
                self.usage()
                sys.exit()
            elif name == '--dumpdoc':
                self.dumpdoc()
                sys.exit()
            elif name == '--api':
                print self.API
                sys.exit()
            elif name in ('-D', '--debug'):
                self.set_debug(True)
            elif name in ('-C', '--config'):
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
                            msg = '%s value must be one of: %s' % (option.long_name, '|'.join(["%s" % str(x) for x in option.choices]))
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

#    def check_for_conflict(self):
#        for option in self.Options:
#            if option.short_name == 'a' or option.short_name == 's':
#                self.access_key_short_name = '-A'
#                self.secret_key_short_name = '-S'
#                opt = self.find_option('--access-key')
#                opt.short_name = 'A'
#                opt = self.find_option('--secret-key')
#                opt.short_name = 'S'

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

    def param_usage(self, plist, label, n=25):
        nn = 80 - n - 13
        if plist:
            print('    %s' % label)
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
                    vv = 'Valid Values: %s' % '|'.join(["%s" % str(x) for x in opt.choices])
                    doclines += textwrap.wrap(vv, nn)
                if doclines:
                    print('        %s%s' % (','.join(names).ljust(n), doclines[0]))
                    for line in doclines[1:]:
                        print('%s%s' % (' ' * (n + 13), line))

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
        print '    %s\n' % self.Description
        # self.synopsis()
        self.param_usage([ opt for opt in self.Options if not opt.optional ],
                         'REQUIRED PARAMETERS')
        self.param_usage([ opt for opt in self.Options if opt.optional ],
                         'OPTIONAL PARAMETERS')
        self.param_usage([ opt for opt in self.StandardOptions ],
                         'STANDARD PARAMETERS')

        if self.Info:
            print self.Info
            
    def dumpdoc(self):
        print '## %s' % self.cmd_name
        print '{:#%s}' % self.cmd_name
        print '\n%s\n' % self.Description

        self.param_usage([ opt for opt in self.Options if not opt.optional ],
                         'REQUIRED PARAMETERS')
        self.param_usage([ opt for opt in self.Options if opt.optional ],
                         'OPTIONAL PARAMETERS')
        if self.Info:
            print self.Info
            
        if self.Examples:
            print "**Examples**"
            print self.Examples
        
    def display_error_and_exit(self, exc):
        try:
            print '%s: %s' % (exc.error_code, exc.error_message, exc.error_detail)
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
            u = urlparse(url)
            if u.scheme.lower() == "https":
                conn = httplib.HTTPSConnection(u.netloc, timeout=timeout)
            else:
                conn = httplib.HTTPConnection(u.netloc, timeout=timeout)
                
            conn.request("GET", u.path + "?" + u.query)
            response = conn.getresponse()
            result = response.read()
            if result:
                return result

#            except httplib.HTTPException as ex:
#                if hasattr(ex, "reason"):
#                    print "HTTPGet: failed to reach a server."
#                    return ex.reason
#                elif hasattr(ex, "code"):
#                    print "HTTPGet: The server couldn\'t fulfill the request."
#                return ex.__str__()

            # if all was well, we won't get here.
            return "No results from request."
        except httplib.ssl.SSLError as ex:
            # a friendlier message if it was a protocol error.
            raise Exception("The protocol specified in the API url property is 'https'.  Is the API really running in SSL mode?")
        except Exception as ex:
            raise ex

    def call_api(self, method, parameters):
        host = self.url
        key = self.access_key
        pw = self.secret_key
        outfmt = "text"
        outdel = ""
        noheader = None
        # was a different output format specified?
        # we limit the values to xml or json.
        if hasattr(self, "output_format"):
            x = getattr(self, "output_format")
            if x:
                if x == "xml" or x == "json":
                    outfmt = x
        # are we using a custom delimiter?
        if hasattr(self, "output_delimiter"):
            x = getattr(self, "output_delimiter")
            if x is not None:
                outdel = x
        # hide the headers in text mode?
        if outfmt == "text":
            noheader = getattr(self, "noheader", None)
        

        
        args = {}
        for param in parameters:
            #if hasattr(self, param):
            if getattr(self, param, None):
                args[param] = getattr(self, param)

        if len(args):
            arglst = ["&%s=%s" % (k, urllib.quote_plus(str(v))) for k, v in args.items()]
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
        od = "&output_delimiter=%s" % urllib.quote_plus(outdel)
        nh = "&header=false" if noheader else ""
        url = "%s/%s%s%s%s%s%s" % (host, string_to_sign, sig, argstr, of, od, nh)
        
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

                        msg = "%s, %s, %s" % (code, message, detail)
                        self.display_error_and_exit(msg)
                    else:
                        # the response might have inner content, or it might have just text
                        try:
                            innercontent = list(xRoot.find("response"))[0]
                            return ET.tostring(innercontent)
                        except IndexError:
                            return xRoot.findtext("response", "")
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
