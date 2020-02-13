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
        print("Please wait ... this could take a while ...")
        self.plugin_name = "teamcity"
        results = self.call_api(self.API, ['plugin_name', 'instance'], timeout=70)
        print(results)
