import ctmcommands.cmd
from ctmcommands.param import Param


class RegisterArtifact(ctmcommands.cmd.CSKCommand):

    Description = 'Record a new revision of a specific Artifact.'
    API = 'register_artifact'
    Examples = '''
    ctm-register-artifact -p "My Project" -n "Artifact One" -l "path/to/artifact" -b master
'''

    Options = [Param(name='project', short_name='p', long_name='project',
                     optional=False, ptype='string',
                     doc='Name or ID of the Project where this Artifact is defined.'),
               Param(name='name', short_name='n', long_name='name',
                     optional=False, ptype='string',
                     doc='Name of the Artifact to revise.'),
               Param(name='branch', short_name='b', long_name='branch',
                     optional=False, ptype='string',
                     doc='Branch in the repository from which this artifact was built.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='Optional version identifier for this Artifact Revision.'),
               Param(name='location', short_name='l', long_name='location',
                     optional=True, ptype='string',
                     doc='Optional location where this Artifact Revision can be found.'),
               Param(name='build_data', short_name='d', long_name='build_data',
                     optional=True, ptype='string',
                     doc='Optional JSON object additional data about the build.')
               ]

    def main(self):
        results = self.call_api(self.API, ['project', 'name', 'branch', 'version', 'location', 'build_data'])
        print(results)
