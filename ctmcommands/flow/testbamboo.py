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
               ]

    def main(self):
        self.plugin = "bamboo.job"
        results = self.call_api(self.API, ['plugin', 'instance'])
        print(results)
