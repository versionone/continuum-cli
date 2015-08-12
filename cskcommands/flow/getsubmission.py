#########################################################################
#
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#
#
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param


class GetSubmission(cskcommands.cmd.CSKCommand):

    Description = """Gets the raw payload of a specific 'Submission' via a MongoDB query.

For query syntax, see the MongDB find() syntax:
http://docs.mongodb.org/manual/reference/method/db.collection.find

Returns the submission document, or a 'not found' message."""

    API = 'get_submission'
    Examples = '''
_To find a Submission using the 'after' property:_

    ccl-get-submission -q '{"after" : "abc123"}'
'''
    Options = [Param(name='query', short_name='q', long_name='query',
                     optional=False, ptype='string',
                     doc='A query in JSON format.')]

    def main(self):
        results = self.call_api(self.API, ['query'])
        print(results)
