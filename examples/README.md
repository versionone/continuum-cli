# Cloud Sidekick Cato Community Edition (CE) Catoclient

## Examples

Cato Client interacts with the Cato CE environment via a REST API.  Command line tools are provided, 
but any of the API calls can be made directly from any technology capable of making HTTP requests.

Cato Client is Python, so there's no shortage of examples.  Included here are basic examples 
in other technologies.

## General Concepts

Making calls to the Cato REST API has a few requirements:

* An _Access Key_ is required.  This will be the 36 character UUID of a Cato user.
* A _Secret Key_ is required.  This will be the password of the Cato User.
* A _URL_ is required.  This is the host and port where the Cato REST API service is running.
* A _Method_ is required.  This is the specific API method being called.

### Signing the Request

All API requests must be signed with a specific mechanism.  Here's an example of a string to be signed:

```
ecoMethods/list_ecosystems?key=0002bdaf-bfd5-4b9d-82d1-fd39c2947d19&timestamp=2012-08-16T15%3A54%3A27
```

The string to sign has the following components:

* key=<access_key> - where <access_key> is a Cato User UUID.
* timestamp=<timestamp> - where <timestamp> is a date and time, _strictly formatted_ like this:
	** 2011-12-20T13%3A58%3A14
	** (Notice the colons in the time portion are URL encoded _before being signed_.)

Once you have the string to sign, encode it as follows:

1.  Create a SHA256 digest (raw mode, not hex) using the appropriate Cato User password as the 'key'.
2.  BASE64 encode the SHA256 digest
3.  URL encode the BASE64 string.

This will give you a signature for the request.
Note: signatures are timely - if the request isn't used quickly the signature will expire.

## Building the URL

Now that we have a signature, we can construct a complete URL.
Once completed, a typical URL will look like this:

```
http://<host:port>/<string_to_sign>&signature=<signature>&<call specific arguments>
```

* <host:port> = for example, localhost:4001. (4001 is the default port for the REST API service, unless customized.)
* <string_to_sign> - the source string used to create the signature.  Nicely, this includes the method, key and timestamp.
* <signature> - the signature completed in the previous steps.
* <call specific arguments> - any additional arguments, in standard _&key=value_ URL format, URL encoded of course!

## Send It!

The final step is to send the request via HTTP.  Obviously, the methods for doing that vary by technology.

## The Response

By default, the Cato REST API returns results in XML format.  This is configurable via the querystring argument:
```
&output_format=<xml|json|text>
```

The XML and JSON responses arrive in a standard _response_ object, with the following attributes:

* method - the method name
* response - the response of the specific method

If there was an error, the following additional attributes will be available:

* error/code - a short error code
* error_message - an error message
* error_detail - verbose error details

### XML

Here's an example of a successful _ecoMethods/get_ecosystem_ request:

```
<apiResponse>
	<method>
		ecoMethods/get_ecosystem
	</method>
	<response>
		<Ecosystem>
			<LastUpdate>
				2012-08-07 14:59:55
			</LastUpdate>
			<Description>
				This is an example Ecosystem.
			</Description>
			<EcotemplateID>
				e7c2c10e-1ee4-43af-847c-034ef34c23d8
			</EcotemplateID>
			<CreatedDate>
				2012-08-07 14:59:55
			</CreatedDate>
			<EcotemplateName>
				My Generic Template
			</EcotemplateName>
			<Name>
				Sample Ecosystem
			</Name>
			<ID>
				1375d4d9-e0c2-11e1-84ac-c8bcc89c1491
			</ID>
		</Ecosystem>
	</response>
</apiResponse>
```

Here's an example of the same request, but with an invalid Ecosystem specified:

```
<apiResponse>
	<method>
		ecoMethods/get_ecosystem
	</method>
	<response />
	<error>
		<code>
			Exception
		</code>
		<message />
		<detail>
			Error getting Ecosystem ID for Name [bogus] - no record found.
		</detail>
	</error>
</apiResponse>
```

### JSON

Here are the same two examples, in JSON format:
_Notice the Response here is also a JSON object, but escaped._

```
{
    "ErrorCode": "",
    "ErrorMessage": "",
    "Method": "ecoMethods/get_ecosystem",
    "ErrorDetail": "",
    "Response": "{\"LastUpdate\": \"2012-08-07 14:59:55\", \"Description\": \"\", \"ParameterXML\": null, \"CloudID\": null, \"NumObjects\": \"0\", \"StormStatus\": \"Error\", \"EcotemplateID\": \"e7c2c10e-1ee4-43af-847c-034ef34c23d8\", \"CreatedDate\": \"2012-08-07 14:59:55\", \"EcotemplateName\": \"Text\", \"Name\": \"foo\", \"StormFile\": \"{\\n    \\\"AWSTemplateFormatVersion\\\": \\\"2010-09-09\\\",\\n    \\\"Description\\\": \\\"AWS CloudFormation Sample Template WordPress_Single_Instance: WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data. It demonstrates using the AWS CloudFormation bootstrap scripts to install packages and files at instance launch time. **WARNING** This template creates an Amazon EC2 instance. You will be billed for the AWS resources used if you create a stack from this template.\\\"\\n}\", \"ID\": \"1375d4d9-e0c2-11e1-84ac-c8bcc89c1491\", \"AccountID\": \"asdf\"}"
}
```

And the error:

```
{
    "ErrorCode": "Exception",
    "ErrorMessage": "",
    "Method": "ecoMethods/get_ecosystem",
    "ErrorDetail": "Error getting Ecosystem ID for Name [ttt] - no record found. ",
    "Response": ""
}
```

## TEXT

Text format is simply a tab delimited, tabular presentation of the response.
Text format is typically used for human readable output.
_Note: Text format does not return identical information as XML/JSON modes.  The Text response may have certain attributes removed for readability._ 