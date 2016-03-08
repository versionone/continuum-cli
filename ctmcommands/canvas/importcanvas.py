#########################################################################
#
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#
#
#########################################################################

import os

import ctmcommands.cmd
from ctmcommands.param import Param

class ImportCanvas(ctmcommands.cmd.CSKCommand):

    Description = 'Imports Canvas items from a properly formatted directory.'
    API = ''
    Examples = ''''''
    Options = [Param(name='inputdirectory', short_name='i', long_name='inputdirectory',
                     optional=True, ptype='string',
                     doc='Directory where the Canvas files exist.  Current directory if omitted.'),
               Param(name='repository', short_name='r', long_name='repository',
                     optional=True, ptype='string',
                     doc=""""Specify either "file" or "db" repository. "db" if omitted. 
                         Only Administrators are allowed to use the "file" option."""),
               Param(name='ignoreconflicts', long_name='ignoreconflicts',
                     optional=True, ptype='boolean',
                     doc="""If provided, the import process will handle Name conflicts aggressively.  
If Canvas items with the same Project/Component/Name exist, they will be overwritten.""")
               ]

    def main(self):
        """
        This command will make multiple API calls.
        
        Rollback on error requires additional API calls.
        
        Basic premise:
        1) spin all the files and create database objects
        2) be happy
        """
        # if no inputdirectory is provided, use the current directory
        rootdir = os.path.expanduser(os.getcwd())
        if self.inputdirectory:
            rootdir = os.path.expanduser(self.inputdirectory)
        # the directory must exist
        if not os.path.exists(rootdir):
            print "The directory [%s] does not exist." % (rootdir)
            return

        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("\nImporting Canvas items could possibly overwrite existing items.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True
        if not go:
            return

        """
        OK, let's keep this clear in our heads... making an API call from a command
            assumes that all the properties of the call are defined as attributes of 'self'.
        
        Some of these property names will be reused across several calls, so be extra sure to keep them updated in context.
        """

        # we're gonna be taking all API responses as JSON
        self.output_format = "json"

        # importing canvas items is pretty easy.
        # 1) The first directory is the 'project'
        # 2) second directory is the component
        # 3) files below that.

        # a flat list of all the details
        everything = []
        projects = [d for d in os.listdir(rootdir) if os.path.isdir(os.path.join(rootdir, d))]
        # filter out any invalid dirs
        projects = [p for p in projects if "proj_" in p]
        if projects:
            for p in projects:
                pdir = os.path.join(rootdir, p)
                components = [d for d in os.listdir(pdir) if os.path.isdir(os.path.join(pdir, d))]
                components = [c for c in components if "comp_" in c]
                if components:
                    for c in components:
                        cdir = os.path.join(pdir, c)
                        files = [f for f in os.listdir(cdir) if os.path.isfile(os.path.join(cdir, f))]
                        files = [f for f in files if "item_" in f]
                        for f in files:
                            # open each file ...
                            fn = os.path.join(cdir, f)
                            with open(fn, 'r') as f_in:
                                if not f_in:
                                    print("Unable to open file [%s]." % fn)
                                data = f_in.read()

                            everything.append((p.replace("proj_", ""), c.replace("comp_", ""), f.replace("item_", ""), data))

        # finally, make the api call for each row (suboptimal I know, but whatever)
        for row in everything:
            self.project, self.component, self.name, self.data = row[:]
            response = self.call_api('create_canvas_item', ['project', 'component', 'name', 'data', 'repository', 'ignoreconflicts'])
            print response

        print "Success!"
