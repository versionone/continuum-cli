#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class ListCanvasItems(ctmcommands.cmd.CSKCommand):

    Description = 'Lists Canvas Items'
    API = 'list_canvas_items'
    Examples = ''''''
    Options = [Param(name='project', short_name='p', long_name='project',
                     optional=True, ptype='string',
                     doc='Filter by a single Canvas Project.'),
               Param(name='component', short_name='c', long_name='component',
                     optional=True, ptype='string',
                     doc='Further filter a Project by Component. (project is required.)'),
               Param(name='repository', short_name='r', long_name='repository',
                     optional=True, ptype='string',
                     doc='Specify either "file" or "db" repository. ("db" if omitted)')]

    def main(self):
        results = self.call_api(self.API, ['project', 'component', 'repository'])
        print(results)
