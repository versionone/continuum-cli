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


class ResubmitChange(ctmcommands.cmd.CSKCommand):

    Description = """Resubmits a previous change 'Submission' to the specified Project.

Identify the submission data using a valid MongoDB query.

For query syntax, see the MongDB find() syntax:
http://docs.mongodb.org/manual/reference/method/db.collection.find

Returns a success or failure."""

    API = 'resubmit_change'
    Examples = '''
_To find a GitHub Webhook using the 'after' property:_

    ctm-resubmit-change -q '{"after" : "abc123"}'
'''
    Options = [Param(name='query', short_name='q', long_name='query',
                     optional=False, ptype='string',
                     doc='A query in JSON format.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = input("Are you sure (y/n)? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            results = self.call_api(self.API, ['query'])
            print(results)
