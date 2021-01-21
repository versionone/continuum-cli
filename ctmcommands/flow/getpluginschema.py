#########################################################################
#
# Copyright 2021 Digital.Ai
# All Rights Reserved.
# https://www.digital.ai
#
#########################################################################
import ctmcommands.cmd
from ctmcommands.param import Param


class GetPluginSchema(ctmcommands.cmd.CSKCommand):

    Description = """Given a valid Plugin name, this API returns the Schema fpr that plugin."""
    API = 'get_plugin_schema'
    Examples = '''
    ctm-get-plugin-schema -p "GitHub"
'''
    Options = [Param(name='plugin_name', short_name='p', long_name='plugin_name',
                     optional=False, ptype='string',
                     doc='Name of the plugin to be returned'),]

    def main(self):
        results = self.call_api(self.API, ['plugin_name'])
        print(results)
