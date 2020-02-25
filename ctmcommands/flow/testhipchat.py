import ctmcommands.cmd
from ctmcommands.param import Param


class TestHipChat(ctmcommands.cmd.CSKCommand):

    Description = "Test HipChat Server connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testhipchat -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='HipChat instance name in the Continuum configuration. Optional, do not use if testing default HipChat instance.'),
               ]

    def main(self):
        print("Please wait ... this could take a while ...")
        self.plugin_name = "hipchatplugin"
        results = self.call_api(self.API, ['plugin_name', 'instance'], timeout=70)
        print(results)
