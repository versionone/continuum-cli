#########################################################################
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
#########################################################################

import os
import setuptools

binscripts = []
for f in os.listdir("bin"):
    binscripts.append("bin/" + f)

setuptools.setup(
    name='continuumclient',
    version='16.2.0',
    description='VersionOne Client Tools',
    author='Patrick Dunnigan',
    author_email='patrick.dunnigan@versionone.com',
    packages=setuptools.find_packages(exclude=['bin']),
    include_package_data=True,
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: No Input/Output (Daemon)',
    ],
    scripts=binscripts,
    py_modules=[])

