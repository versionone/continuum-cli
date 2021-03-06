#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ScheduleTasks(ctmcommands.cmd.CSKCommand):

    Description = 'Schedules one or more Tasks using a json template file.'
    API = 'schedule_tasks'
    Examples = '''
    ctm-schedule-tasks -s ./schedule_template.json
'''
    Options = [Param(name='schedulefile', short_name='s', long_name='schedulefile',
                     optional=False, ptype='string',
                     doc='''The path to a json formatted schedule definition file. See the schedule_tasks API documentation for the format of the file.''')
               ]

    def main(self):
        try:
            # first, we need to load the schedule definition
            self.tasks = None
            if self.schedulefile:
                import os
                fn = os.path.expanduser(self.schedulefile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    self.tasks = f_in.read()

            results = self.call_api(self.API, ['tasks'])
            print(results)
        except Exception as ex:
            raise ex
