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

class InstallLicense(catoclient.catocommand.CatoCommand):

    Description = 'Installs or updates the Cloud Sidekick license by importing a license file'
    API = 'install_license'
    Examples = '''
    maestro-install-license -i "~/maestro_license.lic"
'''
    Options = [Param(name='inputfile', short_name='i', long_name='inputfile',
                     optional=False, ptype='string',
                     doc='Path to a Maestro license.dat file.')]

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
