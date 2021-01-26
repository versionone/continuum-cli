#########################################################################
#
# Copyright 2021 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import json
import ctmcommands.cmd
from ctmcommands.param import Param


class SetProjectDirectives(ctmcommands.cmd.CSKCommand):
    """
    Sets a projects' directives. This removes any already existing directives from the project.

    Example JSON document:

```
{
  "project_id": "5fda00c4c78ea1fe8779cf8e",
  "directives": [
    {
      "type": "jira_workitem_lookup",
      "when": "always",
      "details": {
        "instance_name": ""
      }
    },
    {
      "type": "assign_to_pipeline",
      "when": "always",
      "details": {
        "project": "",
        "group": "a group",
        "definition": "a definition"
      }
    }
  ]
}
```
    """

    Description = """Sets a project's directives from a JSON document.

Returns {"result": "success"} on success."""

    API = 'set_project_directives'
    Examples = ''''''
    Options = [Param(name='directivesfile', short_name='d', long_name='directivesfile',
                     optional=False, ptype='string',
                     doc='A JSON document containing a project_id and directives.')
               ]

    def main(self):
        import os

        directives = None
        if self.directivesfile:
            fn = os.path.expanduser(self.directivesfile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [{}].".format(fn))
                directives = f_in.read()

        results = self.call_api(self.API, data=directives, verb='POST', content_type="application/json")
        print(results)
