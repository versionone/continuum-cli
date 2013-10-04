#########################################################################
# 
# Copyright 2013 Cloud Sidekick
# __________________
# 
#  All Rights Reserved.
# 
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import catoclient.catocommand
from catoclient.param import Param

class AddService(catoclient.catocommand.CatoCommand):

    Description = 'Creates a new Deployment Service.'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='servicefile', short_name='s', long_name='servicefile',
                     optional=False, ptype='string',
                     doc='File name of a JSON Service definition file.')
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nAdding a Service to a running Deployment makes it different from the source Application Template.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            self.service = None
            if self.servicefile:
                import os
                fn = os.path.expanduser(self.servicefile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    data = f_in.read()
                    if data:
                        self.service = data

        results = self.call_api('add_service', ['deployment', 'service'])
        print(results)
