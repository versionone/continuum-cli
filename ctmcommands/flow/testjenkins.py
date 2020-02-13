import ctmcommands.cmd
from ctmcommands.param import Param


class TestJenkins(ctmcommands.cmd.CSKCommand):

    Description = "Test Jenkins connectivity"
    API = "test_plugin_connection"
    Examples = """
    ctm-testjenkins -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Jenkins instance name in the Continuum configuration. Optional, do not use if testing default Jenkins instance.'),
               ]

    def main(self):
        print("Please wait ... this could take a while ...")
        self.plugin_name = "jenkins"
        results = self.call_api(self.API, ['plugin_name', 'instance'], timeout=70)
        print(results)
