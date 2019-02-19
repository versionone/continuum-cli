import ctmcommands.cmd
from ctmcommands.param import Param


class ExportProgression(ctmcommands.cmd.CSKCommand):

    Description = 'Export a Progression Definition as a portable backup JSON document.'
    API = 'export_progression'
    Examples = '''
    ctm-export-progression -p "Some Progression Name"
'''
    Options = [Param(name='progression', short_name='p', long_name='progression',
                     optional=False, ptype='string',
                     doc='Value can be either a Progression Definition ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['progression'])
        print(results)
