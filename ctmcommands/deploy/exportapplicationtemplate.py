#########################################################################
# 
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
# 
# 
#########################################################################

import os
import json
import base64

import ctmcommands.cmd
from ctmcommands.param import Param


class ExportApplicationTemplate(ctmcommands.cmd.CSKCommand):

    Description = 'Exports an Application Template to a directory.'
    API = 'export_application_template'
    Examples = '''
_To export an application template to a directory_

    ctm-export-application-template -t "MyApp" -v "1" -o "./myapp"
'''
    Options = [Param(name='template', short_name='t', long_name='template',
                     optional=False, ptype='string',
                     doc='Name of the Application Template.'),
               Param(name='version', short_name='v', long_name='version',
                     optional=False, ptype='string',
                     doc='The Application Template Version.'),
               Param(name='outputdirectory', short_name='o', long_name='outputdirectory',
                     optional=True, ptype='string',
                     doc='Directory where the output will be saved.  The directory must exist, and should be empty.'),
               Param(name='printoutput', short_name='p', long_name='printoutput',
                     optional=True, ptype='boolean',
                     doc='If provided, no file will be created.  The results of the API call will be printed.')
               ]

    def main(self):
        """
        OK a few notes here.
        
        1) We are absolutely NOT creating or emptying directories.  Doing so would allow a user to 
            make a huge mistake passing in a directory like /etc and pooching the whole box.
            
        2) The directory must exist, and *should* be empty.  
        
        3) We will create the subdirectories, but if they or any files already exist we'll just leave them be.
        
        """
        # if no outputdirectory was provided, we will just print the results
        if self.printoutput:
            results = self.call_api(self.API, ['template', 'version'])
            print(results)
            return

        # if no outputdirectory is provided, use the current directory
        rootdir = os.getcwd()
        if self.outputdirectory:
            rootdir = os.path.expanduser(self.outputdirectory)

        # the directory must exist
        if not os.path.exists(rootdir):
            print "The directory [%s] does not exist." % (rootdir)
            return
            
        # create subdirectories
        defdir = os.path.join(rootdir, "definition")
        if not os.path.exists(defdir):
            os.makedirs(defdir)
        icondir = os.path.join(rootdir, "icon")
        if not os.path.exists(icondir):
            os.makedirs(icondir)
        taskdir = os.path.join(rootdir, "tasks")
        if not os.path.exists(taskdir):
            os.makedirs(taskdir)
        reportdir = os.path.join(rootdir, "reports")
        if not os.path.exists(reportdir):
            os.makedirs(reportdir)
        
        results = self.call_api(self.API, ['template', 'version'])

        # so, the result MIGHT be json and it MIGHT be an error message.
        # we don't know... so let's trap the json parse and show the result if it fails
        appbackup = None
        try:
            appbackup = json.loads(results)
        except:
            print(results)
            return
        
        if not appbackup:
            print("Unable to continue - API returned no export document. %s" % (results))
            return
        
        # first, write the application details JSON file.
        app_details = {}
        app_details["Name"] = appbackup["Name"]
        app_details["Version"] = appbackup["Version"]
        app_details["Description"] = appbackup["Description"]

        fn = os.path.join(rootdir, "application.json")
        with open(fn, 'w+') as f_out:
            if not f_out:
                print("Unable to open file [%s]." % fn)
            f_out.write(json.dumps(app_details))

        # the definition json            
        if appbackup.get("Definition"):
            fn = os.path.join(defdir, "definition.json")
            with open(fn, 'w+') as f_out:
                if not f_out:
                    print("Unable to open file [%s]." % fn)
                f_out.write(appbackup.get("Definition"))
        
        # the icon
        if appbackup.get("Icon"):
            # we don't know what format the image is, just use png it's ok.
            fn = os.path.join(icondir, "application.png")
            with open(fn, 'w+') as f_out:
                if not f_out:
                    print("Unable to open file [%s]." % fn)
                f_out.write(base64.b64decode(appbackup.get("Icon")))
        
        # now, spin each task and write a file for it
        for t in appbackup.get("Tasks", []):
            # parse the json to a dict, read the taskname for the filename, but save the original raw text
            tobj = json.loads(t)
            
            # ok, we want a fairly readable filename from the task name, which could contain anything
            # so this little bit of wizardry should give us a sane filename
            keepcharacters = ('.', '_')
            taskfilename = "".join(c for c in tobj["Name"] if c.isalnum() or c in keepcharacters).strip()
            fn = os.path.join(taskdir, "%s.json" % taskfilename)
            with open(fn, 'w+') as f_out:
                if not f_out:
                    print("Unable to open file [%s]." % fn)
                f_out.write("%s\n" % (t))
        
        # write all the report files
        projs = appbackup.get("Reports", [])
        for p in projs:
            # create the project dir
            pdir = os.path.join(reportdir, "proj_%s" % (p["Name"]))
            if not os.path.exists(pdir):
                os.makedirs(pdir)
            
            # Components
            for c in p["Components"]:
                # create the category dir 
                cdir = os.path.join(pdir, "comp_%s" % (c["Name"]))
                if not os.path.exists(cdir):
                    os.makedirs(cdir)

                # Files
                for i in c["Items"]:
                    # write this file into the category directory
                    filename = "item_%s" % (i["Name"])
                    fn = os.path.join(cdir, filename)
                    with open(fn, 'w+') as f_out:
                        if not f_out:
                            print("Unable to open file [%s]." % fn)
                        f_out.write(i["Data"])
