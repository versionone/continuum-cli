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
               ]

    def main(self):
        self.plugin = "octopus.octo"
        results = self.call_api(self.API, ['plugin', 'instance'])
        print(results)
