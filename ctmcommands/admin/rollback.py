import ctmcommands.cmd
from ctmcommands.param import Param
from subprocess import Popen, PIPE
import os


class Rollback(ctmcommands.cmd.CSKCommand):

    Description = '''Rollback Continuum to a previously installed release.'''
    API = 'rollback'
    Examples = '''
    ctm-rollback -v 16.0.400
'''
    Options = [Param(name='version', short_name='v', long_name='version',
                     optional=True, ptype='string',
                     doc='An explicit official release version to install.')]

    def main(self):
        if not self.version:
            print "\nRollback version is required.\n"
            exit()

        _newlink = "/opt/continuum/ctm-%s-x86_64" % (self.version)
        # is it a valid target directory?
        if not os.path.isdir(_newlink):
            print("\nSpecified version [%s] is not installed.\n\nCheck /opt/continuum for available versions to rollback.\n" % (self.version))
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
            p = Popen(["ctm-stop-services"], stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()
            print(o)
            print(e)
            
            # relink
            p = Popen(["rm", "/opt/continuum/clearcode"], stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()
            print(o)
            print(e)
            p = Popen(["ln", "-s", _newlink, "/opt/continuum/clearcode"], stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()
            print(o)
            print(e)

            # start
            p = Popen(["ctm-start-services"], stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()
            print(o)
            print(e)
