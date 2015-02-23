#########################################################################
# 
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import cskcommands.cmd
from cskcommands.param import Param

class InstallLicense(cskcommands.cmd.CSKCommand):

    Description = 'Installs or updates the ClearCode license by importing a license file'
    API = 'install_license'
    Examples = '''
    ccl-install-license -i "~/csk_license.lic"
'''
    Options = [Param(name='inputfile', short_name='i', long_name='inputfile',
                     optional=False, ptype='string',
                     doc='Path to a license.dat file.')]

    def main(self):
        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("WARNING: This is an administrative function.\n\nUpdating the license cannot be undone.\n\nAre you sure? ")
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            self.license = None
            if self.inputfile:
                import os
                fn = os.path.expanduser(self.inputfile)
                with open(fn, 'r') as f_in:
                    if not f_in:
                        print("Unable to open file [%s]." % fn)
                    data = f_in.read()
                    if data:
                        self.license = data

            results = self.call_api(self.API, ['license'])
            print(results)
