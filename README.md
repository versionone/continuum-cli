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

```
python setup.py install
```

## Usage

No installation instructions or setuptools script is done yet. In the
meantime, perform the following command before using the command line
utilities:

```
export PYTHONPATH=<pathtolibrary>/catoclient
```

Then to run the command line tool:

```
<pathtolibrary>/catoclient/bin/cato-list-tasks --url=http://localhost:4001 --access-key=<catouseruuid> --secret-key <catopassword> 
```

### Configuration File

A configuration file option is available to save common options (url, credentials, etc).
The file, .catoclient.conf, is in json format, and is looked for in your $HOME directory (~/.catoclient.conf).
Any values entered in this file become defaults for all commands.
Typically this will include the url and access_key.

An additional option, --config_file=foo.conf, allows you to specify a different json configuration file.
This allows you to save your secret_key, if desired, in a different directory.

Any arguments passed on the command line take precedence over values stored in config files.

_NOTE: It's never a smart idea to save your secret key in a file, however the option is available._

If url and credentials are put in the config file, then the commands can be executed more simply:

```
<pathtolibrary>/catoclient/bin/cato-list-tasks
```



See individual commands for usage.
