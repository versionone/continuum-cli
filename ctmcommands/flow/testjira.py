import ctmcommands.cmd
from ctmcommands.param import Param


class TestJira(ctmcommands.cmd.CSKCommand):

    Description = "Test Jira connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testjira -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Jira instance name in the Continuum configuration. Optional, do not use if testing default Jira instance.'),
               ]

    def main(self):
        print("Please wait ... this could take a while ...")
        self.plugin_name = "jiraplugin"
        results = self.call_api(self.API, ['plugin_name', 'instance'], timeout=70)
        print(results)
