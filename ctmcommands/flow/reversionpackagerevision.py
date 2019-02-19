import ctmcommands.cmd
from ctmcommands.param import Param


class ReversionPackageRevision(ctmcommands.cmd.CSKCommand):

    Description = 'Changes the Version of the specified (and all matching previous) Package Revisions.'
    API = 'reversion_packagerevision'
    Examples = '''
    ctm-reversion-packagerevision -p "Some Package Name" -r 205 -v 15.1

    - or -

    ctm-promote-revision -p "Some Package Name" -f "15.2.3.205" -v 15.1
'''
    Options = [Param(name='package', short_name='p', long_name='package',
                     optional=False, ptype='string',
                     doc='Name of the Package to promote to a Progression Phase.'),
               Param(name='revision', short_name='r', long_name='revision',
                     optional=True, ptype='string',
                     doc='Revision number of a Package to promote, takes precedence over "full_version".'),
               Param(name='full_version', short_name='f', long_name='full_version',
                     optional=True, ptype='string',
                     doc='Optional Full Version of package to promote, optional alternative selector to "revision".'),
               Param(name='new_version', short_name='v', long_name='new_version',
                     optional=False, ptype='string',
                     doc='Optional "new version" for this and all prior revisions of this Package.')
               ]

    def main(self):
        results = self.call_api(self.API, ['package', 'revision', 'full_version', 'new_version'])
        print(results)
