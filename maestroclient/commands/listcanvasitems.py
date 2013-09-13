#########################################################################
# 
# Copyright 2013 Cloud Sidekick
# __________________
# 
#  All Rights Reserved.
# 
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import catoclient.catocommand
from catoclient.param import Param

class ListCanvasItems(catoclient.catocommand.CatoCommand):

    Description = 'Lists Canvas Items'
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
        results = self.call_api('list_canvas_items', ['project', 'component', 'repository'])
        print(results)
