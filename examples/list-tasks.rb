#!/usr/bin/env ruby

require "net/http"
require "uri"
require "openssl"
require "base64"


host = "http://localhost:8080/api"
method = "list_tasks"
access_key = ""
secret_key = ""

if host == ""
    abort("HOST not provided.")
elsif method == ""
    abort("METHOD not provided.")
elsif access_key == ""
    abort("ACCESS_KEY not provided.")
elsif secret_key == ""
    abort("SECRET_KEY not provided.")
end

#timestamp
ts = (Time.now).utc.strftime("%Y-%m-%dT%H:%M:%S")
ts = ts.gsub(":", "%3A")

#string to sign
string_to_sign = "#{method}?key=#{access_key}&timestamp=#{ts}"

digest = OpenSSL::Digest::Digest.new("sha256")
hmac = OpenSSL::HMAC.digest(digest, secret_key, string_to_sign)
#sig = Base64.urlsafe_encode64(hmac)
sig = Base64.encode64(hmac)
sig = sig.gsub("=", "%3D").gsub("/", "%2F").gsub("+", "%2B")
sig = "&signature=#{sig}"


# build the URL
url = "#{host}/#{string_to_sign}#{sig}"
puts "Getting #{url}"

# go get it
uri = URI.parse(url)
response = Net::HTTP.get_response(uri)
puts response
