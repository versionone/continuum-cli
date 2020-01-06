#########################################################################
# Copyright 2019 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import os
import json

import ctmcommands.cmd
from ctmcommands.param import Param


class ExportCanvas(ctmcommands.cmd.CSKCommand):

    Description = 'Exports Canvas items to a directory.'
    API = 'export_canvas'
    Examples = ''''''
    Options = [Param(name='project', short_name='p', long_name='project',
                     optional=True, ptype='string',
                     doc='If provided, limits export to a specific Project.'),
               Param(name='component', short_name='c', long_name='component',
                     optional=True, ptype='string',
                     doc='If provided, limits a Project to a specific Component. (project is required.)'),
               Param(name='repository', short_name='r', long_name='repository',
                     optional=True, ptype='string',
                     doc='Specify either "file" or "db" repository. ("db" if omitted.)'),
               Param(name='outputdirectory', short_name='o', long_name='outputdirectory',
                     optional=True, ptype='string',
                     doc='Directory where the output will be saved.  The directory must exist, and should be empty.'),
               Param(name='printoutput', long_name='printoutput',
                     optional=True, ptype='boolean',
                     doc='If provided, no file will be created.  The results of the API call will be printed.')
               ]

    def main(self):
        """
        The API call will return a list of project items.

        Save them all in the proper directory structure.

        """

        # if no outputdirectory was provided, we will just print the results
        if self.printoutput:
            results = self.call_api(self.API, ['project', 'component'])
            print(results)
            return

        # if no outputdirectory is provided, use the current directory
        rootdir = os.getcwd()
        if self.outputdirectory:
            rootdir = os.path.expanduser(self.outputdirectory)

        # the directory must exist
        if not os.path.exists(rootdir):
            print("The directory [%s] does not exist." % (rootdir))
            return

        results = self.call_api(self.API, ['project', 'component', 'repository'])

        # the result MIGHT be an error!!! in which case the json.loads will fail
        try:
            projs = json.loads(results)
        except:
            print(results)
            return

        if not projs:
            print("No results found.")
            return

        for p in projs:
            # create the project dir
            print("Project: %s" % (p["Name"]))
            pdir = os.path.join(rootdir, "proj_%s" % (p["Name"]))
            if not os.path.exists(pdir):
                os.makedirs(pdir)

            # Components
            for c in p["Components"]:
                print("    Component: %s" % (c["Name"]))
                # create the category dir
                cdir = os.path.join(pdir, "comp_%s" % (c["Name"]))
                if not os.path.exists(cdir):
                    os.makedirs(cdir)

                # Files
                for i in c["Items"]:
                    print("        Item: %s" % (i["Name"]))
                    # write this file into the category directory
                    filename = "item_%s" % (i["Name"])
                    fn = os.path.join(cdir, filename)
                    with open(fn, 'w+') as f_out:
                        if not f_out:
                            print("Unable to open file [%s]." % fn)
                        f_out.write(i["Data"].encode("utf-8", "ignore") if i["Data"] else "")

        print("Project(s) successfully backed up to [%s]." % (rootdir))
