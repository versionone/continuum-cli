import ctmcommands.cmd
from ctmcommands.param import Param


class DeliverPackageRevision(ctmcommands.cmd.CSKCommand):

    Description = '`Delivers` a Package Revision out of a Progression into a Delivered condition.'
    API = 'deliver_revision'
    Examples = '''
    ctm-deliver-packagerevision -p "Some Package Name" -r 205

    - or -

    ctm-deliver-revision -p "Some Package Name" -f "15.2.3.205"
'''
    Options = [Param(name='package', short_name='p', long_name='package',
                     optional=False, ptype='string',
                     doc='Name of the Package to promote to a Progression Phase.'),
               Param(name='revision', short_name='r', long_name='revision',
                     optional=True, ptype='string',
                     doc='Revision number of a Package to promote, takes precedence over "full_version".'),
               Param(name='full_version', short_name='f', long_name='full_version',
                     optional=True, ptype='string',
                     doc='Optional Full Version of package to promote, optional alternative selector to "revision".')
               ]

    def main(self):
        results = self.call_api(self.API, ['package', 'revision', 'full_version'])
        print(results)
