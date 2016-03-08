#########################################################################
#
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class GetSubmission(ctmcommands.cmd.CSKCommand):

    Description = """Gets the raw payload of a specific 'Submission' via a MongoDB query.

For query syntax, see the MongDB find() syntax:
http://docs.mongodb.org/manual/reference/method/db.collection.find

Returns the submission document, or a 'not found' message."""

    API = 'get_submission'
    Examples = '''
_To find a Submission using the 'after' property:_

    ctm-get-submission -q '{"after" : "abc123"}'
'''
    Options = [Param(name='query', short_name='q', long_name='query',
                     optional=False, ptype='string',
                     doc='A query in JSON format.')]

    def main(self):
        results = self.call_api(self.API, ['query'])
        print(results)
