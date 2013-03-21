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

### Passing Credentials via Command Line

Each command accepts Cato web service api connection parameters as command line arguments as follows. 

```
cato-list-tasks --url=http://localhost:4001 --access-key=<catouseruuid> --secret-key <catopassword> 
```

### Configuration File

Alternatively configuration file option is available to save common options (url, credentials, etc).
The file, .catoclient.conf, is in json format, and is looked for in your $HOME directory (~/.catoclient.conf).
Any values entered in this file become defaults for all commands.
Typically this will include the url and access_key.

An additional option, --config_file=foo.conf, allows you to specify a different json configuration file.
This allows you to save your secret_key, if desired, in a different directory.

Any arguments passed on the command line take precedence over values stored in config files.

_NOTE: It's never a smart idea to save your secret key in a file, however the option is available._

If url and credentials are put in the config file, then the commands can be executed more simply:

```
cato-list-tasks
```

Example .catoclient.conf file:
```
{
    "url": "http://ec2-54-234-163-202.compute-1.amazonaws.com:4001",
    "access_key": "username",
    "secret_key2: "password"
}
```
## Documentation

Visit the [Cato Client wiki pages](https://github.com/cloudsidekick/catoclient/wiki) for more information on individual command usage.
