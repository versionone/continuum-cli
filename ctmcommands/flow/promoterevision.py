import ctmcommands.cmd
from ctmcommands.param import Param


class PromoteRevision(ctmcommands.cmd.CSKCommand):

    Description = 'Promotes a Package Revision to a particular Phase.'
    API = 'promote_revision'
    Examples = '''
    ctm-promote-revision -p "Some Package Name" -r 205 -h "Regression Testing"

    - or -

    ctm-promote-revision -p "Some Package Name" -f "15.2.3.205" -h "Regression Testing"
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
               Param(name='phase', short_name='h', long_name='phase',
                     optional=False, ptype='string',
                     doc='Name of the Phase to which the specified Package Revision will be promoted.'),
               Param(name='new_version', short_name='v', long_name='new_version',
                     optional=True, ptype='string',
                     doc='Optional "new version" for this and all prior revisions of this Package.')
               ]

    def main(self):
        results = self.call_api(self.API, ['package', 'revision', 'full_version', 'phase', 'new_version'])
        print(results)
