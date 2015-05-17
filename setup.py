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


from setuptools import setup

install_requires = [
    'cloudify-plugins-common==3.2',
    'cloudify-rest-client==3.2',
    'cloudify-script-plugin==1.2',
    'cloudify-diamond-plugin==1.2',
    'click==4.0',
    'celery==3.1.17',
    'jinja2==2.7.2',
    'pywinrm==0.0.3',
    'fabric==1.8.3'
]

setup(
    name='cloudify-agent',
    version='3.3',
    author='Gigaspaces',
    author_email='cloudify@gigaspaces.com',
    packages=[
        'cloudify_agent',
        'cloudify_agent.api',
        'cloudify_agent.api.pm',
        'cloudify_agent.api.plugins',
        'cloudify_agent.installer',
        'cloudify_agent.installer.config',
        'cloudify_agent.installer.runners',
        'cloudify_agent.shell',
        'cloudify_agent.shell.commands'
    ],
    package_data={
        'cloudify_agent': [
            'resources/pm/initd/celeryd.conf.template',
            'resources/pm/initd/celeryd.template',
            'resources/pm/initd/disable-requiretty.sh']
        },
    description='Cloudify Agent Implementation (Celery based)',
    install_requires=install_requires,
    license='LICENSE',
    entry_points={
        'console_scripts': [
            'cfy-agent = cloudify_agent.shell.main:main',
        ]
    }
)