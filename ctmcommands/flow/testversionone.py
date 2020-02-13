import ctmcommands.cmd
from ctmcommands.param import Param


class TestVersionOne(ctmcommands.cmd.CSKCommand):

    Description = "Test VersionOne connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testversionone -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='VersionOne instance name in the Continuum configuration. Optional, do not use if testing default VersionOne instance.'),
               ]

    def main(self):
        print("Please wait ... this could take a while ...")
        self.plugin_name = "v1plugin"
        results = self.call_api(self.API, ['plugin_name', 'instance'], timeout=70)
        print(results)
