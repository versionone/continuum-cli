import ctmcommands.cmd
from ctmcommands.param import Param


class TestTeamCity(ctmcommands.cmd.CSKCommand):

    Description = "Test TeamCity connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testteamcity -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='TeamCity instance name in the Continuum configuration. Optional, do not use if testing default TeamCity instance.'),
               ]

    def main(self):
        self.plugin = "teamcity.job"
        results = self.call_api(self.API, ['plugin', 'instance'])
        print(results)
