import cskcommands.cmd
from cskcommands.param import Param
from subprocess import Popen, PIPE
import os


class Rollback(cskcommands.cmd.CSKCommand):

    Description = '''Rollback Continuum to a previously installed release.'''
    API = 'rollback'
    Examples = '''
    ccl-rollback -v 16.0.400
'''
    Options = [Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An explicit official release version to install.')]

    def main(self):
        if not self.version:
            print "\nRollback version is required.\n"
            exit()

        _newlink = "/opt/ccl/ccl-%s-x86_64" % (self.version)
        # is it a valid target directory?
        if not os.path.isdir(_newlink):
            print("\nSpecified version [%s] is not installed.\n\nCheck /opt/ccl for available versions to rollback.\n" % (self.version))
            exit()

        go = False
        if self.force:
            go = True
        else:
            answer = raw_input("""
Rolling back Continuum will restart all services.

Make sure all activity has stopped and all users are aware.

Are you sure? """)
            if answer:
                if answer.lower() in ['y', 'yes']:
                    go = True

        if go:
            # stop
            p = Popen(["ccl-stop-services"], stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()
            print(o)
            print(e)
            
            # relink
            p = Popen(["rm", "/opt/ccl/clearcode"], stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()
            print(o)
            print(e)
            p = Popen(["ln", "-s", _newlink, "/opt/ccl/clearcode"], stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()
            print(o)
            print(e)

            # start
            p = Popen(["ccl-start-services"], stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()
            print(o)
            print(e)
