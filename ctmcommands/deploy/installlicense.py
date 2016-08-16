#########################################################################
# 
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class InstallLicense(ctmcommands.cmd.CSKCommand):

    Description = 'Installs or updates the Continuum license by importing a license file'
    API = 'install_license'
    Examples = '''
    ctm-install-license -i "~/license.lic"
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
