import ctmcommands.cmd
from ctmcommands.param import Param


class TestOpenShift(ctmcommands.cmd.CSKCommand):

    Description = "Test OpenShift connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testopenshift -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Instance name in the Continuum configuration. Optional, not necessary if testing the default instance.'),
               ]

    def main(self):
        self.plugin = "openshift.main"
        results = self.call_api(self.API, ['plugin', 'instance'])
        print(results)
