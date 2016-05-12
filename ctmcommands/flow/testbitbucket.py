import ctmcommands.cmd
from ctmcommands.param import Param


class TestBitBucket(ctmcommands.cmd.CSKCommand):

    Description = "Test BitBucket connectivity"
    API = "test_bitbucket"
    Examples = """
    ctm-testbitbucket -i instancename
"""
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=True, ptype='string',
                     doc='Instance name in the Continuum configuration. Optional, not necessary if testing the default instance.'),
               ]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
