import ctmcommands.cmd
from ctmcommands.param import Param


class TestSonarqube(ctmcommands.cmd.CSKCommand):

    Description = "Test Sonarqube connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testsonarqube -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Sonarqube instance name in the Continuum configuration. Optional, do not use if testing default Sonarqube instance.'),
               ]

    def main(self):
        self.plugin = "sonarqube.sonarqube"
        results = self.call_api(self.API, ['plugin', 'instance'])
        print(results)
