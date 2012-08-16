#!/usr/bin/env tclsh

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

package require base64
package require sha256  1.0.2
package require tdom
package require http
#package require tls
#::http::register https 443 ::tls::socket

# This script will list all Tasks.

set ::API_URL [lindex [split [lindex $::argv 0]] 0]
set ::KEY [lindex [split [lindex $::argv 1]] 0]
set ::PASSWORD [lindex [split [lindex $::argv 2]] 0]
set ::SILENT [lindex [split [lindex $::argv 3]] 0]
set ::RESULT ""

proc output {args} {
	if {"$::SILENT" != "-silent"} {
		set output_string [lindex $args 0]
		#puts "\n[clock format [clock seconds] -format "%Y-%m-%d %H:%M:%S"] :: $output_string"
		puts "$output_string"
		flush stdout
	}
}

proc http_get {url} {
	catch {set token [::http::geturl $url -timeout [expr 60 * 1000]]} error_code
	
	if {[string match "::http::*" $error_code] == 0} {
		set output_buffer "<error>$error_code</error>"
		#output "\n\nHTTP Error:\n$error_code" 1
	} else {
		if {"[::http::status $token]" != "ok" || [::http::ncode $token] != 200} {
			set output_buffer "<error>HTTP Error: [::http::status $token] [::http::code $token] [::http::data $token]</error>"
		} else {
			set output_buffer [::http::data $token]
		}
		
	}
	if {[info exists token] == 1} {
		::http::cleanup $token 
	}

	set ::RESULT $output_buffer
}

#############
# MAIN CODE #
#############

output "Cato ListTasks Utility\n"

# do not continue unless we have all the required arguments
if {"$::API_URL" == "" || "$::KEY" == "" || "$::PASSWORD" == ""} {
	output "Usage:\n list-tasks.tcl <url> <key> <password>\n\nExample:\n list-tasks.tcl localhost:4001 550e8400-e29b-41d4-a716-446655440000 foo"
	exit
}

# a little useful information
output "Using the API at: $::API_URL"
output "API Key: $::KEY"

### SIGNING THE REQUEST

# timestamp must be this exact format, in UTC time, and with the dashes URL encoded
# 2011-12-20T13%3A58%3A14
set timestamp [string map {: %3A} [clock format [clock seconds] -format "%Y-%m-%dT%H:%M:%S" -gmt true]]
#output "Timestamp: $timestamp"

set string_to_sign "taskMethods/list_tasks?key=$::KEY&timestamp=$timestamp"
#output "String to sign: $string_to_sign"

# SHA256 the string_to_sign using the password
set signature [::sha2::hmac -bin $::PASSWORD $string_to_sign]

# base64 encode it (no wraps)
set signature [base64::encode -wrapchar "" $signature]

# then, url encode it.
# replace occurences of http reserved characters in the base64 encoding, 
# because a base64 string can include three invalid HTTP chars (+, / and =).
# + becomes %2B
# / becomes %2F
# = becomes %3D
set signature  [string map {= %3D / %2F + %2B} $signature]
#output "Signature: $signature"

# build the URL we will connect to
set url "http://$::API_URL/$string_to_sign&signature=$signature"

output "\n\nConnecting using: $url"

# and do the connection
http_get $url

# here are the results!
output $::RESULT

# and we're done
exit
