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

class AddServiceToSequenceStep(catoclient.catocommand.CatoCommand):

    Description = 'Adds a service to a Deployment Sequence Step.'
    Options = [Param(name='deployment', short_name='d', long_name='deployment',
                     optional=False, ptype='string',
                     doc='Value can be either an deployment id or deployment name.'),
               Param(name='sequence', short_name='s', long_name='sequence',
                     optional=False, ptype='string',
                     doc='A Sequence name on this Deployment.'),
               Param(name='step', short_name='t', long_name='step',
                     optional=False, ptype='int',
                     doc='The step number on which to add the Service.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=False, ptype='string',
                     doc='The name or ID of the new Service.'),
               Param(name='desired', short_name='e', long_name='desired',
                     optional=False, ptype='string',
                     doc='The Desired State.'),
               Param(name='initial', short_name='i', long_name='initial',
                     optional=False, ptype='string',
                     doc='The Initial State.')]

    def main(self):
        results = self.call_api('depMethods/add_service_to_sequence_step', ['deployment', 'sequence', 'step', 'service', 'desired', 'initial'])
        print(results)
