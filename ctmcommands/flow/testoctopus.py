import ctmcommands.cmd
from ctmcommands.param import Param


class TestOctopus(ctmcommands.cmd.CSKCommand):

    Description = "Test Octopus connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testoctopus -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Octopus instance name in the Continuum configuration. Optional, do not use if testing default Octopus instance.'),
               Param(name='team', short_name='t', long_name='team',
                     optional=True, ptype='string',
                     doc="The Team to search for the Plugin Instance to use. Defaults to plugins available to All Teams."),
               ]

    def main(self):
        print("Please wait ... this could take a while ...")
        self.plugin_name = "octopus"
        results = self.call_api(self.API, ['plugin_name', 'instance'], timeout=70)
        print(results)
