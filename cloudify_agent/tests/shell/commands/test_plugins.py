#########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.

import mock

from cloudify_agent.tests.shell.commands import BaseCommandLineTestCase


@mock.patch('cloudify_agent.api.plugins.installer.PluginInstaller.install')
class TestConfigureCommandLine(BaseCommandLineTestCase):

    def test_install(self, mock_install):
        self._run('cfy-agent plugins install --source=source --args=args')
        mock_install.assert_called_once_with('source', 'args')