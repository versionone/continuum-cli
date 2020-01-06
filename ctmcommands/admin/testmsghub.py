#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import websocket

import ctmcommands.cmd
from ctmcommands.param import Param


class TestMessageHub(ctmcommands.cmd.CSKCommand):

    Description = 'Sends a test alert message to the UI.'
    API = ''
    Examples = '''
_To send an email to an email address_

    ctm-test-messagehub -u ws://10.0.0.1:8083
'''
    Options = [Param(name='server', short_name='s', long_name='server',
                     optional=False, ptype='string',
                     doc='URL of the Continuum server.  Use "wss" if Continuum is running in SSL mode, otherwise use "ws".  Use the port as configured, or the default of 8083.')
               ]

    def main(self):
        _url = "%s/pub/admin" % (self.server)
        print(("Publishing a message to [%s]..." % (_url)))
        ws = websocket.WebSocket(sslopt={"cert_reqs": 0})
        ws.connect(_url)
        msg = '''{
            "type": "alert",
            "msg": "This is a test message through the Message Hub service."
        }'''
        ws.send(msg)
        result = ws.recv()
        print("Received %s" % result)
        ws.close()
