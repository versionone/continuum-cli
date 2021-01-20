#########################################################################
#
# Copyright 2021 Digital.Ai
# All Rights Reserved.
# https://www.digital.ai
#
#########################################################################
import ctmcommands.cmd
from ctmcommands.param import Param


class AddProjectSource(ctmcommands.cmd.CSKCommand):

    Description = """ Adds a "Changes from" source to a Project. Will also mark a Project type as "Source".
    > Returns a CTM endpoint """
    API = 'add_project_source'
    Examples = '''
    ctm-add-project-source -p "ProjectName" -o "github"
'''
    Options = [Param(name='project', short_name='p', long_name='project',
                     optional=False, ptype='string',
                     doc='Value can be either a Project ID or Name.'),
                Param(name='origin', short_name='o', long_name='origin',
                     optional=False, ptype='string',
                     doc='Name of VCS to add to Project.'),
                Param(name='secret', short_name='s', long_name='secret',
                     optional=True, ptype='string',
                     doc='Webhook secret for GitHub.'),]

    def main(self):
        results = self.call_api(self.API, ['project', 'origin', 'secret'])
        print(results)
