---
title: "IOOS Registry - API"
layout: single
excerpt: "IOOS Registry - API"
sitemap: false
permalink: /pages/registry/api/
---
The registry exposes an API based on
[Restivus](https://github.com/kahmali/meteor-restivus) to allow users to
automatically trigger a harvest job. This is useful for users that wish to
integrate the IOOS registry into an automated workflow.

## API v1

The version one API contains all the public accessor methods. 

### /api/v1/Harvests

_Note: the Harvests in the URL needs to be capitalized._

This endpoint accepts HTTP GET requests and responds with the JSON listing of
each Harvest document and metadata associated with that harvest.

Here's an example with curl:

    curl https://registry.ioos.us/api/v1/Harvests

A response looks like:

    {
      "status": "success",
      "data": [
        {
          "_id": "n3N6xBLyZIs9LGwEF",
          "harvest_type": "WAF",
          "name": "PacIOOS WAF",
          "url": "http://www.pacioos.hawaii.edu/metadata/iso/",
          "publish": true,
          "harvest_interval": 1,
          "organization": "PacIOOS",
          "last_harvest_dt": "2017-04-27T00:05:01.717Z",
          "ckan_harvest_url": "http://dev-catalog.ioos.us/harvest/pacioos-waf",
          "last_record_count": 802,
          "last_good_count": 801,
          "last_bad_count": 1,
          "last_harvest_status": "ok"
        }
    }

## API v2


### /api/v2/login

In order to generate an API token with the registry you must authenticate yourself. The endpoint accepts HTTP posts with the following parameters:

- `email` - The user's email used for logging in
- `password` - This can be either a hashed password using sha256 or plaintext
- `hashed` - set to `true` if using the sha256 hashed password in the password field.

Here's an example with curl:

    curl -i -d 'email=me@email.com&password=sha-256-password&hashed=true' -XPOST https://registry.ioos.us/api/v2/login

Sending a plaintext password is highly discouraged.

The response from the server will be an authentication token that can be used in other API requests:

    { status: "success", data: {authToken: "f2KpRW7KeN9aPmjSZ", userId: "fbdpsNf4oHiX79vMJ"} }


### /api/v2/logout

This API endpoint is used to invalidate an exisitng Authentication Token.

The endpoint is an authenticated endpoint and requires the following HTTP headers to be set:

- `X-Auth-Token` - The authentication token obtained from login
- `X-User-Id` - The User ID obtained from login

Here's an example with curl:

  curl -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -i https://registry.ioos.us/api/v2/logout


### /api/v2/harvest/`<harvest_id>`/harvest

This API endpoint will initiate a new harvest job for the harvest object with
the identifier matching `<harvest_id>`.

The endpoint is an authenticated endpoint and requires the following HTTP headers to be set:

- `X-Auth-Token` - The authentication token obtained from login
- `X-User-Id` - The User ID obtained from login

Here's an example with curl:

    curl -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -i https://registry.ioos.us/api/v2/harvest/abc123/harvest
