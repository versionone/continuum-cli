import cskcommands.cmd
from cskcommands.param import Param
import os
import stat
import requests
import shutil
import subprocess


class Update(cskcommands.cmd.CSKCommand):

    Description = '''Update Continuum to the latest official release, or alternatively select a specific release.'''
    API = 'update'
    Examples = '''
    ccl-update
    
    ccl-update -v 16.0.400
    
    cclupdate -d 16.1.503
'''
    Options = [Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An explicit official release version to install.'),
               Param(name='development', short_name='d', long_name='development',
                     optional=True, ptype='string',
                     doc='A specific development version to install.')]

    def main(self):
        if self.version and self.development:
            print "\nCannot specify both a release version and a development version.\n"
            exit()

        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("""
Updating Continuum will restart all services.

Make sure all activity has stopped and all users are aware.

Are you sure? """)
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            _url = None
            _file = "/tmp/continuum-installer.sh"
            if self.version:
                print("Downloading official release %s..." % (self.version))
                _url = "http://downloads.clearcodelabs.com.s3.amazonaws.com/clearcode-%s-installer.sh" % (self.version)
            elif self.development:
                print("Downloading development build %s..." % (self.development))
                _url = "https://s3.amazonaws.com/builds.clearcodelabs.com/installer/clearcode-%s-x86_64-installer.sh" % (self.development)
            else:
                print("Downloading the latest release...")
                _url = "http://downloads.clearcodelabs.com.s3.amazonaws.com/clearcode-latest-installer.sh"
                
            r = requests.get(_url, stream=True)
            if r.status_code == 200:
                with open(_file, "wb") as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                    
            st = os.stat(_file)
            os.chmod(_file, st.st_mode | stat.S_IEXEC)

            p = subprocess.Popen([_file, "-s"], stdout=subprocess.PIPE)
            while True:
                output = p.stdout.readline()
                if output == '' and p.poll() is not None:
                    break
                if output:
                    print output.strip()
