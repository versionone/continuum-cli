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


class SetPIGroupNumber(ctmcommands.cmd.CSKCommand):

    Description = """Set the autonumber root on Pipeline Instance Group. (Used to issue ascending numbers to Instances in the Group.)

Requires the '_id' of the Pipeline Instance Group and the new number value to set.

Returns success or failure."""

    API = 'set_pipelinegroup_number'
    Examples = ''''''
    Options = [Param(name='pg', short_name='i', long_name='pg',
                     optional=False, ptype='string',
                     doc='ID of a Pipeline Instance Group.'),
               Param(name='newnumber', short_name='n', long_name='newnumber',
                     optional=False, ptype='string',
                     doc='New Number to set.')               
               ]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("Are you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['pg', 'newnumber'])
            print(results)
