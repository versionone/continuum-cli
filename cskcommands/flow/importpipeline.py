import cskcommands.cmd
from cskcommands.param import Param


class ImportPipeline(cskcommands.cmd.CSKCommand):

    Description = """Imports a Pipeline Definition from a JSON document.

Returns a Pipeline Object."""

    API = 'import_pipeline'
    Examples = ''''''
    Options = [Param(name='backupfile', short_name='b', long_name='backupfile',
                     optional=False, ptype='string',
                     doc='A JSON document formatted as a complete CSK Pipeline Definition backup.'),
               Param(name='overwrite', short_name='o', long_name='overwrite',
                     optional=True, ptype='string',
                     doc="""Valid values: pipeline|phases|all|none (default).""")
               ]

    def main(self):
        import os

        self.backup = None
        if self.backupfile:
            fn = os.path.expanduser(self.backupfile)
            with open(fn, 'r') as f_in:
                if not f_in:
                    print("Unable to open file [%s]." % fn)
                self.backup = f_in.read()

        results = self.call_api(self.API, ['backup', 'overwrite'], verb='POST')
        print(results)
