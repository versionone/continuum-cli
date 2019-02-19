import ctmcommands.cmd
from ctmcommands.param import Param


class ExportPackage(ctmcommands.cmd.CSKCommand):

    Description = 'Export a Package Definition as a portable backup JSON document.'
    API = 'export_package'
    Examples = '''
    ctm-export-package -p "Some Package Name"
'''
    Options = [Param(name='package', short_name='p', long_name='package',
                     optional=False, ptype='string',
                     doc='Value can be either a Package Definition ID or Name.')]

    def main(self):
        results = self.call_api(self.API, ['package'])
        print(results)
