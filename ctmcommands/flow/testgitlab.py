import ctmcommands.cmd
from ctmcommands.param import Param


class TestGitlab(ctmcommands.cmd.CSKCommand):

    Description = "Test GitLab connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testgitlab -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Instance name in the Continuum configuration. Optional, not necessary if testing the default instance.'),
               ]

    def main(self):
        self.plugin = "gitlab.gitlab"
        results = self.call_api(self.API, ['plugin', 'instance'])
        print(results)
