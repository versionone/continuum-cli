# Cloud Sidekick Cato Community Edition (CE) Catoclient

## Description

The Catoclient is a command line toolset for accessing the Cato CE 
web service. It also provides a Python sdk for programmatically 
interacting with the web service.

## Repository and Download

https://github.com/cloudsidekick/catoclient

To download _the latest_ source:

```
curl -Lk --output catoclient.tar.gz https://github.com/cloudsidekick/catoclient/tarball/master
```

Specific release tarballs are here:

https://github.com/cloudsidekick/catoclient/tags

or clone in git:

```
git clone git://github.com/cloudsidekick/catoclient.git
```

## Bug and Feature Requests

https://github.com/cloudsidekick/catoclient/issues

## Requirements

Python 2.6+ 

## Installation

TBD

## Usage

No installation instructions or setuptools script is done yet. In the
meantime, perform the following command before using the command line
utilities:

```
export PYTHONPATH=<pathtolibrary>/catoclient
```

Then to run the command line tool:

```
<pathtolibrary>/catoclient/bin/cato-list-ecosystems --url=http://localhost:4001 --access-key=<catouseruuid> --secret-key <catopassword> 
```

See individual commands for usage.
