import ctmcommands.cmd
from ctmcommands.param import Param


class GetPackageManifest(ctmcommands.cmd.CSKCommand):

    Description = 'Get the Manifest of a Package, for the specified version and range of revisions.'
    API = 'get_package_manifest'
    Examples = '''
    ctm-get-package-manifest -p "Some Package Name" -v "Specific Version" -f "From Revision" -t "To Revision"
'''
    Options = [Param(name='package', short_name='p', long_name='package',
                     optional=False, ptype='string',
                     doc='Value can be either a Package Definition ID or Name.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='Optional Package Version. (All Versions if omitted.)'),
               Param(name='from', short_name='f', long_name='from',
                     optional=True, ptype='string',
                     doc='From Revision. (First (oldest) Revision in the range if omitted.)'),
               Param(name='to', short_name='t', long_name='to',
                     optional=True, ptype='string',
                     doc='To Revision. (Last (newest) Revision in the range if omitted.)'),
               Param(name='to', short_name='t', long_name='to',
                     optional=True, ptype='string',
                     doc='To Revision. (Last (newest) Revision in the range if omitted.)'),
               Param(name='verbose', long_name='verbose',
                     optional=True, ptype='boolean',
                     doc='Verbose data for result objects.')
               ]

    def main(self):
        results = self.call_api(self.API, ['package', 'version', 'from', 'to', 'verbose'])
        print(results)
