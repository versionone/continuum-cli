#########################################################################
#
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class RerunPipelineInstance(ctmcommands.cmd.CSKCommand):

    Description = """Rerun an Instance, using the saved 'initial data'.

Returns a Pipeline Instance object."""

    API = "rerun_pipelineinstance"
    Examples = """"""
    Options = [
        Param(
            name="pi",
            short_name="i",
            long_name="pi",
            optional=False,
            ptype="string",
            doc="Name or ID of a Pipeline Instance.",
        )
    ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("Are you sure (y/n)? ")
            if answer:
                if answer.lower() in ["y", "yes"]:
                    go = True

        if go:
            results = self.call_api(self.API, ["pi"])
            print(results)
