#########################################################################
# Copyright 2011 Cloud Sidekick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#########################################################################

import catoclient.catocommand
from catoclient.param import Param

class SendMessage(catoclient.catocommand.CatoCommand):

    Description = 'Sends a message to a User or email address.'
    Options = [Param(name='to', short_name='t', long_name='to',
                     optional=False, ptype='string',
                     doc='Comma-separated Users or addresses.'),
               Param(name='subject', short_name='s', long_name='subject',
                     optional=False, ptype='string',
                     doc='Subject of the message.'),
               Param(name='message', short_name='m', long_name='message',
                     optional=False, ptype='string',
                     doc='Content of the message.',),
               Param(name='cc', short_name='c', long_name='cc',
                     optional=True, ptype='string',
                     doc='Comma-separated Users or addresses to CC.'),
               Param(name='bcc', short_name='b', long_name='bcc',
                     optional=True, ptype='string',
                     doc='Comma-separated Users or addresses to BCC.')
               ]

    def main(self):
        results = self.call_api('send_message', ['to', 'subject', 'message', 'cc', 'bcc'])
        print(results)
