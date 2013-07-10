#!/usr/bin/env python

import urllib
import urllib2
from datetime import datetime
import hashlib
import base64
import hmac


host = "http://localhost:4001"
method = "list_tasks"
access_key = ""
secret_key = ""

if not host:
    raise Exception("HOST not provided.")
if not method:
    raise Exception("METHOD not provided.")
if not access_key:
    raise Exception("ACCESS_KEY not provided.")
if not secret_key:
    raise Exception("SECRET_KEY not provided.")


args = {} # a dictionary of any arguments required for the method
if args:
    arglst = ["&%s=%s" % (k, urllib.quote_plus(v)) for k, v in args.items()]
    argstr = "".join(arglst)
else:
    argstr = ""

#timestamp
ts = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
ts = ts.replace(":", "%3A")

#string to sign
string_to_sign = "{0}?key={1}&timestamp={2}".format(method, access_key, ts)

#encoded signature
sig = base64.b64encode(hmac.new(str(secret_key), msg=string_to_sign, digestmod=hashlib.sha256).digest())
sig = "&signature=" + urllib.quote_plus(sig)


url = "%s/%s%s%s" % (host, string_to_sign, sig, argstr)

print "Trying an HTTP GET to %s" % url

response = urllib2.urlopen(url, None, 10)
result = response.read()
if result:
    print result
else:
    print "No response."
