import ctmcommands.cmd
from ctmcommands.param import Param


class TestBamboo(ctmcommands.cmd.CSKCommand):

    Description = "Test Bamboo connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testbamboo -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Bamboo instance name in the Continuum configuration. Optional, do not use if testing default Bamboo instance.'),
               Param(name='team', short_name='t', long_name='team',
                     optional=True, ptype='string',
                     doc="The Team to search for the Plugin Instance to use. Defaults to plugins available to All Teams."),
               ]

    def main(self):
        print("Please wait ... this could take a while ...")
        self.plugin_name = "bamboo"
        results = self.call_api(self.API, ['plugin_name', 'instance'], timeout=70)
        print(results)
