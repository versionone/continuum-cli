import os
import json
import decimal
import string
import ctmcommands.cmd
from ctmcommands.param import Param
import shutil


indent = "        "


def AsJSON(dict_obj):
    return json.dumps(dict_obj, default=jsonSerializeHandler, indent=4, sort_keys=True, separators=(',', ': '))


def jsonSerializeHandler(obj):
    # decimals
    if isinstance(obj, decimal.Decimal):
        return float(obj)

    # date time
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        return str(obj)


def format_teamname_to_dirname(team_name):
    valid_chars = "-_@'. %s%s" % (string.ascii_letters, string.digits)
    dirname = ''.join(c for c in team_name if c in valid_chars)
    dirname = dirname.replace(' ', '_')
    dirname = dirname.replace('@', '_')
    dirname = dirname.replace("'", "_")
    return dirname


def remove_illegal_chars_in_filename(file_name):
    valid_chars = string.letters + string.digits + " -_."
    valid_file_name = ""
    unique_str = ""

    for index, char in enumerate(file_name):
        if char in valid_chars:
            valid_file_name += char
        else:
            unique_str += str(index) + str(ord(char))

    return (valid_file_name, unique_str)


def create_file(dir, file_label, asset):
    print "%sItem: %s" % (indent, file_label)

    if "/" in file_label or "\\" in file_label:
        print("{0}{0}{1} contains a slash in its name. ".format(indent, file_label))
        print("{0}{0}Skipping...".format(indent))
        return

    valid_file_name, unique_str = remove_illegal_chars_in_filename(file_label)

    # write this file into the category directory
    try:
        if valid_file_name != file_label:
            valid_file_name += "_" + unique_str

        fn = os.path.join(dir, valid_file_name + ".json")
        with open(fn, 'w+') as f_out:
            if not f_out:
                print("Unable to open file [%s]." % fn)
            f_out.write(AsJSON(asset))
    except Exception as ex:
        print("{0}{0}Error handling Item {1}".format(indent, file_label))
        print("{0}{0}{1}".format(indent, ex))
        print("{0}{0}Skipping...".format(indent))


class ExportCatalog(ctmcommands.cmd.CSKCommand):

    Description = 'Export all Project, Pipeline, Package, and Task definitions to a catalog as JSON documents.'
    API = 'export_catalog'
    Examples = '''
_To export a catalog of backup files._

    ctm-export-catalog -o myoutputdirectory -t "teamname or teamid"
'''
    Options = [Param(name='outputdirectory', short_name='o', long_name='outputdirectory',
                     optional=True, ptype='string',
                     doc='Directory where the output will be saved.  The directory must exist, and should be empty.'),
               Param(name='team', short_name='t', long_name='team',
                     optional=True, ptype='string',
                     doc='''Team "name" or id, To export the assets of specified team. 
                            Multiple teams can be specified using comma. E.g. "Dev Team","Test Team"'''),
               ]

    def save_assets_in_file(self, assets, asset_type, root_dir, team_dir_list):
        for asset in assets:
            if asset_type == "tasks":
                team_name = format_teamname_to_dirname(asset.get("Team"))
                asset_name = "{}_{}".format(asset.get("Name"), asset.get("Version"))
            else:
                team_name = format_teamname_to_dirname(asset.get("team"))
                asset_name = asset.get("name")
            team_dir = os.path.join(root_dir, team_name)
            asset_type_dir = os.path.join(team_dir, asset_type)

            if team_name not in team_dir_list:
                if os.path.isdir(team_dir):
                    shutil.rmtree(team_dir)
                team_dir_list.append(team_name)

            if not os.path.exists(asset_type_dir):
                os.makedirs(asset_type_dir)

            create_file(asset_type_dir, asset_name, asset)

    def main(self):
        # if no outputdirectory is provided, use the current directory
        if self.outputdirectory:
            rootdir = os.path.expanduser(self.outputdirectory)
        else:
            rootdir = os.path.join(os.getcwd(), "continuum_export")
            if not os.path.exists(rootdir):
                os.makedirs(rootdir)

        # the directory must exist
        if not os.path.exists(rootdir):
            print "The directory [%s] does not exist." % (rootdir)
            return

        response = self.call_api(self.API, ['team'], timeout=300)
        # the result MIGHT be an error!!! in which case the json.loads will fail
        try:
            results = json.loads(response)
        except:
            print response
            return

        if not results:
            print "No results found."
            return

        team_dir_list = []
        print("Projects")
        self.save_assets_in_file(results.get("projects", []), "projects", rootdir, team_dir_list)

        print("Packages")
        self.save_assets_in_file(results.get("packages", []), "packages", rootdir, team_dir_list)

        print("Pipelines")
        self.save_assets_in_file(results.get("pipelines", []), "pipelines", rootdir, team_dir_list)

        print("Tasks")
        self.save_assets_in_file(results.get("tasks", []), "tasks", rootdir, team_dir_list)
