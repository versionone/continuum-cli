#########################################################################
# 
# Copyright 2013 Cloud Sidekick
# __________________
# 
#  All Rights Reserved.
# 
# NOTICE:  All information contained herein is, and remains
# the property of Cloud Sidekick and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Cloud Sidekick
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Cloud Sidekick.
#
#########################################################################

import os
import setuptools

from catoclient import __version__

binscripts = []
for f in os.listdir("bin"):
    binscripts.append("bin/"+f)

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
    scripts=binscripts,
    py_modules=[])

