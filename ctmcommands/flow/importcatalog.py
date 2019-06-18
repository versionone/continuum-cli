import os
import json
import string
import sys
import ctmcommands.cmd
from ctmcommands.param import Param

indent = "        "


def read_dir(dir):
    dir_content = []
    for file in os.listdir(dir):
        file_content = read_file(dir, file)
        if file_content:
            dir_content.append(file_content)
    return dir_content


def read_file(dir, file):
    file_path = os.path.join(dir, file)
    try:
        with open(file_path, 'r') as f_in:
            print "%sFile: %s" % (indent, file)
            if not f_in:
                print("Unable to open file [%s]." % file)
                return None
            return json.loads(f_in.read())
    except Exception as ex:
        print("{0}{0}Error handling Item {1}".format(indent, file))
        print("{0}{0}{1}".format(indent, ex))
        print("{0}{0}Skipping...".format(indent))


def get_dirname_for_team(team_name):
    valid_chars = "-_@'. %s%s" % (string.ascii_letters, string.digits)
    dirname = ''.join(c for c in team_name if c in valid_chars)
    dirname = dirname.replace(' ', '_')
    dirname = dirname.replace('@', '_')
    dirname = dirname.replace("'", "_")
    return dirname


class ImportCatalog(ctmcommands.cmd.CSKCommand):

    Description = 'Import all Project, Pipeline, Package, and Task definitions from a catalog as JSON documents.'
    API = 'import_catalog'
    GetUserTeamsAPI = 'get_user_teams'
    Examples = '''
_To import a catalog from backup files._

    ctm-import-catalog -i myinputdirectory -t "teamname or teamid"
'''
    Options = [Param(name='inputdirectory', short_name='i', long_name='inputdirectory',
                     optional=True, ptype='string',
                     doc='Directory where the input files are located.  The directory must exist.'),
               Param(name='team', short_name='t', long_name='team',
                     optional=True, ptype='string',
                     doc='''Team "name" or id, To import the assets in specified team. 
                                Multiple teams can be specified using comma. E.g. "Dev Team","Test Team"'''),
               Param(name='overwrite', short_name='o', long_name='overwrite',
                     optional=True, ptype='string',
                     doc="""Valid values: true|false (default)."""),
               Param(name='human_readable', short_name='h', long_name='humanreadable',
                     optional=True, ptype='string',
                     doc="""Valid values: true (default)|false."""),
               Param(name='import_into_team', short_name='I', long_name='import_into_team',
                     optional=True, ptype='string',
                     doc='''Team "name" or id. If specified, the catalog will be imported into the specified team, rather than the teams specified in the input files.
                                This may be useful if you wish to import items from another team or Continuum instance'''),
               ]

    def main(self):
        # if no inputdirectory is provided, use the current directory
        if self.inputdirectory:
            rootdir = os.path.expanduser(self.inputdirectory)
        else:
            rootdir = os.path.join(os.getcwd(), "continuum_export")
            if not os.path.exists(rootdir):
                os.makedirs(rootdir)

        # the directory must exist
        if not os.path.exists(rootdir):
            print "The directory [%s] does not exist." % (rootdir)
            return

        import_dict = {
            'overwrite': self.overwrite,
            'human_readable': self.human_readable,
            'import_into_team': self.import_into_team,
        }
        res_teams = json.loads(self.call_api(self.GetUserTeamsAPI)).get("teams")
        user_teams = {team["team_id"]: team["name"] for team in res_teams}
        team_dirs = []

        if self.team:
            if "," in self.team:
                teamname_or_ids = self.team.split(",")
            else:
                teamname_or_ids = [self.team]

            for teamname_or_id in teamname_or_ids:
                try:
                    team_dirs.append(get_dirname_for_team(user_teams[teamname_or_id]))
                except KeyError:
                    for name in user_teams.itervalues():
                        if name == teamname_or_id:
                            team_dirs.append(get_dirname_for_team(teamname_or_id))
                            break

            len_valid_teamdirs = len(team_dirs)
            if len_valid_teamdirs == 0:
                sys.exit("Invalid Team(s)")
            elif len_valid_teamdirs < len(teamname_or_ids):
                no_of_invalid_teams = len(teamname_or_ids) - len_valid_teamdirs
                print "Found %d Invalid Team(s)" % int(no_of_invalid_teams)
            else:
                pass
        else:
            team_dirs = os.listdir(rootdir)

        print("Projects")
        project_json = []
        for team_dir in team_dirs:
            # Read the projects dir
            proj_dir = os.path.join(rootdir, team_dir, "projects")
            if os.path.exists(proj_dir):
                project_json.extend(read_dir(proj_dir))

        if project_json:
            import_dict["projects"] = project_json

        print("Packages")
        package_json = []
        for team_dir in team_dirs:
            # Read the packages dir
            pkg_dir = os.path.join(rootdir, team_dir, "packages")
            if os.path.exists(pkg_dir):
                package_json.extend(read_dir(pkg_dir))

        if package_json:
            import_dict["packages"] = package_json

        print("Pipelines")
        pipeline_json = []
        for team_dir in team_dirs:
            # Read the pipelines dir
            pipe_dir = os.path.join(rootdir, team_dir, "pipelines")
            if os.path.exists(pipe_dir):
                pipeline_json.extend(read_dir(pipe_dir))

        if pipeline_json:
            import_dict["pipelines"] = pipeline_json

        print("Tasks")
        task_json = []
        for team_dir in team_dirs:
            # Read the tasks dir
            task_dir = os.path.join(rootdir, team_dir, "tasks")
            if os.path.exists(task_dir):
                task_json.extend(read_dir(task_dir))

        if task_json:
            import_dict["tasks"] = task_json

        if self.team:
            import_dict['team'] = self.team

        response = self.call_api(self.API, data=json.dumps(import_dict), verb='POST', content_type="application/json")
        print response
