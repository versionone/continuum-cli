#!/usr/bin/env python

import os
import sys
import json
import urllib
import urllib2
from datetime import datetime
import hashlib
import base64
import hmac
import argparse

base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))
lib_path = os.path.join(base_path, "lib")
sys.path.insert(0, lib_path)

parser = argparse.ArgumentParser(description='Connect to the API.')
parser.add_argument('--host', help='The host url of the API service.')
parser.add_argument('--method', '-m', help='The method to call.')
parser.add_argument('--accesskey', '-k', help='The access key for the request.')
parser.add_argument('--secretkey', '-s', help='The secret key for the request.')
parser.add_argument('--querystring', '-q', help='Direct entry of querystring arguments.')
parser.add_argument('--file', '-f', type=argparse.FileType('r'), help='Method and arguments.')

# if we wanna get additional items from argparse, try "parser.parse_known_args()" instead
cmdlineargs, randomargs = parser.parse_known_args()
methodargs = None

# load the specified definition file if provided...
if cmdlineargs.file:
    methodargs = json.loads(cmdlineargs.file.read())

# the command line overrides any similar values from the json file.
# but the json file isn't actually required
host = cmdlineargs.host
method = cmdlineargs.method
access_key = cmdlineargs.accesskey
secret_key = cmdlineargs.secretkey
querystring = cmdlineargs.querystring
args = {}
files = {}

if methodargs:
    host = methodargs["url"] if "url" in methodargs and not cmdlineargs.host else cmdlineargs.host
    method = methodargs["method"] if "method" in methodargs and not cmdlineargs.method else cmdlineargs.method
    access_key = methodargs["access_key"] if "access_key" in methodargs and not cmdlineargs.accesskey else cmdlineargs.accesskey
    secret_key = methodargs["secret_key"] if "secret_key" in methodargs and not cmdlineargs.secretkey else cmdlineargs.secretkey
    args = methodargs["args"] if "args" in methodargs else {}
    files = methodargs["files"] if "files" in methodargs else {}

# Some API calls require one or more big arguments, too much to pass in
# the method file.  So, anything in the 'files' section of the method file is opened
# and added to the args dictionary using the key name provided.
# NOTE: file contents are always base64 encoded for HTTP...
# ... the receiving methods know which arguments to decode.

if files:
    for k, v in files.items():
        with open(v, 'r') as f_in:
            if not f_in:
                print("Unable to open file [%s]." % v)
            data = f_in.read()
            if data:
                args[k] = packData(data)

# Finally, a little magic here... if any unexpected args are passed, they'll be in the randomargs list.
# there's no formatting there, so we're expecting the user to be smart enough to 
# put them in the key=value format
# we will append them to our global 'args' dictionary
# NOTE: if any values have the same key as something defined in the json file, 
# these will take precedence, which is what we want.
print randomargs
if randomargs:
    for pair in randomargs:
        print pair
        if "=" in pair:
            k, v = pair.split("=", 1)
            args[k] = v



def http_get(url, timeout=10):
    try:
        if not url:
            return "URL not provided."
        
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

def call_api(host, method, key, pw, args):
    try:
        if not host:
            return "HOST not provided."
        if not method:
            return "METHOD not provided."
        if not key:
            return "ACCESSKEY not provided."
        if not pw:
            return "SECRETKEY not provided."

        if host.endswith('/'):
            host = host[:-1]

        if args:
            arglst = ["&%s=%s" % (k, urllib.quote_plus(v)) for k, v in args.items()]
            argstr = "".join(arglst)
        else:
            argstr = ""
        
        # timestamp
        ts = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
        ts = ts.replace(":", "%3A")

        # string to sign
        string_to_sign = "{0}?key={1}&timestamp={2}".format(method, key, ts)
        
        # encoded signature
        sig = base64.b64encode(hmac.new(str(pw), msg=string_to_sign, digestmod=hashlib.sha256).digest())
        sig = "&signature=" + urllib.quote_plus(sig)
        

        url = "%s/%s%s%s" % (host, string_to_sign, sig, argstr)
        
        # NOTE: if a --querystring was passed on the command line, we just use it, no questions asked
        if querystring:
            url += "&%s" % querystring
            
        return http_get(url)
    except Exception as ex:
        raise ex

def packData(sIn):
    # NOTE: this encoding scheme must match what's defined in the server code.
    # ( in the catocommon package )
    sOut = base64.b64encode(str(sIn))
    return sOut.replace("/", "%2F").replace("+", "%2B")

# make the call
result = call_api(host, method, access_key, secret_key, args)

print result
