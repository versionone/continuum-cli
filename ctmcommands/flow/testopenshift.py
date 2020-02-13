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
               Param(name='team', short_name='t', long_name='team',
                     optional=True, ptype='string',
                     doc="The Team to search for the Plugin Instance to use. Defaults to plugins available to All Teams."),
               ]

    def main(self):
        print("Please wait ... this could take a while ...")
        self.plugin_name = "openshift"
        results = self.call_api(self.API, ['plugin_name', 'instance'], timeout=70)
        print(results)
