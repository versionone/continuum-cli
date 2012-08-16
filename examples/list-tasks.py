#!/usr/bin/env python

import urllib
import urllib2
from datetime import datetime
import hashlib
import base64
import hmac


host = "http://localhost:4001"
method = "taskMethods/list_tasks"
access_key = "0002bdaf-bfd5-4b9d-82d1-fd39c2947d19"
secret_key = "c4t4lyss"
args = {} # a dictionary of any arguments required for the method


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
        
        #timestamp
        ts = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
        ts = ts.replace(":", "%3A")

        #string to sign
        string_to_sign = "{0}?key={1}&timestamp={2}".format(method, key, ts)
        
        #encoded signature
        sig = base64.b64encode(hmac.new(str(pw), msg=string_to_sign, digestmod=hashlib.sha256).digest())
        sig = "&signature=" + urllib.quote_plus(sig)
        

        url = "%s/%s%s%s" % (host, string_to_sign, sig, argstr)
        
        return http_get(url)
    except Exception as ex:
        raise ex


# make the call
result = call_api(host, method, access_key, secret_key, args)

print result
