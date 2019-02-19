import ctmcommands.cmd
from ctmcommands.param import Param


class GetPackage(ctmcommands.cmd.CSKCommand):

    Description = 'Get the definition document of a Package.'
    API = 'get_package'
    Examples = '''
    ctm-get-get_package-manifest -p "Some Package Name"
'''
    Options = [Param(name='package', short_name='p', long_name='package',
                     optional=False, ptype='string',
                     doc='Value can be either a Package Definition ID or Name.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['package'])
        print(results)
