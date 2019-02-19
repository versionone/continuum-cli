#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class CreateWebhook(ctmcommands.cmd.CSKCommand):

    Description = 'Creates a new Outbound Webhook configuration.'
    API = 'create_webhook'
    Examples = '''
    ctm-create-webhook -n "MyApplication" -u "http://my.application.net/api/send_here"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='The name of the Webhook'),
               Param(name='destinationurl', short_name='d', long_name='destinationurl',
                     doc='URL of the REST API endpoint. ex: http://my.application.net/api/send_here',
                     optional=True)]

    def main(self):
        results = self.call_api(self.API, ['name', 'destinationurl'])
        print(results)
