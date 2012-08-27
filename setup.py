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

import os
import setuptools

from catoclient import __version__

setuptools.setup(
    name='catoclient',
    version = __version__,
    description='Cloud Sidekick Cato Community Edition (CE) Catoclient',
    license='Apache License (2.0)',
    author='Patrick Dunnigan',
    author_email='patrick.dunnigan@cloudsidekick.com',
    url='https://github.com/cloudsidekick/catoclient',
    #cmdclass=setup.get_cmdclass(),
    packages=setuptools.find_packages(exclude=['bin']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: No Input/Output (Daemon)',
    ],
    scripts=['bin/cato-create-ecosystem',
            'bin/cato-create-ecotemplate',
            'bin/cato-describe-task-parameters',
            'bin/cato-get-active-tasks',
            'bin/cato-get-ecosystem',
            'bin/cato-get-ecosystem-actions',
            'bin/cato-get-ecosystem-log',
            'bin/cato-get-ecosystem-objects',
            'bin/cato-get-ecotemplate',
            'bin/cato-get-task',
            'bin/cato-get-task-instance',
            'bin/cato-get-task-instance-status',
            'bin/cato-get-task-instances',
            'bin/cato-get-task-log',
            'bin/cato-get-task-parameters-template',
            'bin/cato-list-cloud-accounts',
            'bin/cato-list-clouds',
            'bin/cato-list-ecosystems',
            'bin/cato-list-ecotemplates',
            'bin/cato-list-methods',
            'bin/cato-list-processes',
            'bin/cato-list-tasks',
            'bin/cato-run-ecosystem-action',
            'bin/cato-run-task',
            'bin/cato-stop-task',
            'bin/cato-version'],
    py_modules=[])

