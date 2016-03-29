import ctmcommands.cmd
from ctmcommands.param import Param


class ExportProject(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a Project Definition for export.'
    API = 'export_project'
    Examples = '''
    ctm-export-project -p "ProjectName" > myproject.json
'''
    Options = [Param(name='project', short_name='p', long_name='project',
                     optional=False, ptype='string',
                     doc='Value can be either a Project ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['project'])
        print(results)
