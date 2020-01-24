#########################################################################
# Copyright 2019 VersionOne
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
    version='19.0.1',
    description='VersionOne Client Tools',
    author='VersionOne',
    author_email='ContinuumAdmin@versionone.com',
    packages=setuptools.find_packages(exclude=['bin']),
    include_package_data=True,
    install_requires=['requests', 'future'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Environment :: No Input/Output (Daemon)',
    ],
    scripts=binscripts,
    py_modules=[])
