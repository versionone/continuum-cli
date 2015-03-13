#########################################################################
# Copyright 2015 ClearCode Labs
# All Rights Reserved.
# http://www.clearcodelabs.com/license.html
#########################################################################

import os
import setuptools

binscripts = []
for f in os.listdir("bin"):
    binscripts.append("bin/" + f)

setuptools.setup(
    name='cclclient',
    version='1.42',
    description='ClearCode Client Tools',
    license='Apache License (2.0)',
    author='Patrick Dunnigan',
    author_email='patrick.dunnigan@clearcodelabs.com',
    url='https://github.com/cloudsidekick/client',
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

