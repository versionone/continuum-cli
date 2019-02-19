import ctmcommands.cmd
from ctmcommands.param import Param


class ExportPlugins(ctmcommands.cmd.CSKCommand):

    Description = 'Export Plugin configurations as a portable backup JSON document.'
    API = 'export_plugins'
    Examples = '''
    ctm-export-plugin -n "Specific Plugin Name"
'''
    Options = [Param(name='name', short_name='n', long_name='name',
                     optional=True, ptype='string',
                     doc='Optional name to export only a specified Plugin.')]

    def main(self):
        results = self.call_api(self.API, ['name'])
        print(results)
