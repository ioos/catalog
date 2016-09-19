---
title: "Best practices for creating Web Accessible Folders (WAFs)"
layout: single
excerpt: "Web Accessible Folder Creation"
sitemap: false
permalink: /pages/registry/waf_creation/
---

## What is a WAF? ##

A WAF stands for a web-accessible folder.  It is any folder with file contents
exposed via a webserver to the outside world.

WAFs for the registry should have a folder named after the parent organization in lowercase.
WAFs should currently only be one level deep in hierarchy.  Files contained
within the WAF should be XML files conforming to the ISO 19115-2 metadata standard.
Ideally, files should be validated to ensure compliance with the standard,
(See, for example, [http://mrdata.usgs.gov/validation/](http://mrdata.usgs.gov/validation/))
although datasets which do not perfectly validate will still be harvested.

### THREDDS ISO support ###

Although the WAF parser can in theory follow external links, it is preferred
to have WAF directories instead point to files hosted on the same server.  For
THREDDS to generate ISO XML files, ncISO must be enabled.

See http://www.unidata.ucar.edu/software/thredds/current/tds/reference/ncISO.html
for details on how to enable ncISO.

Once enabled, export the file to the folder with the WAF, either through
manually using a web browser to save ISOs of interest or using a tool such as
`wget`: <br />

```
wget "http://dm1.caricoos.org/thredds/iso/buoys/RealTime/PR1/DSG_PR1.accelerometer2.realtime.nc?catalog=http%3A%2F%2Fdm1.caricoos.org%2Fthredds%2Fcatalog%2Fbuoys%2FRealTime%2FPR1%2Fcatalog.html&dataset=buoys%2FRealTime%2FPR1%2FDSG_PR1.accelerometer2.realtime.nc" -O "dest_dir/RealTime_FPR1_DSG_PR1.accelerometer2.realtime.xml"
```

### Hosting a WAF on a webserver. ###

These directions assume you have a folder on a filesystem with ISOs stored
within.

## Apache `.conf` files ##

In the .conf files, use the +Indexes directive

```
<Directory /usr/local/apache2/htdocs/listme>
  Options +Indexes
</Directory>
```

See: [https://wiki.apache.org/httpd/DirectoryListings](https://wiki.apache.org/httpd/DirectoryListings)

## Nginx ##

Inside of the `server` block, put the `autoindex on` inside the appropriate location block where the WAF directory is contained:

```
location /somedir {
       autoindex on;
}
```

See [http://nginx.org/en/docs/http/ngx_http_autoindex_module.html](http://nginx.org/en/docs/http/ngx_http_autoindex_module.html)

## IIS

[https://technet.microsoft.com/en-us/library/cc725840%28v=ws.10%29.aspx](https://technet.microsoft.com/en-us/library/cc725840%28v=ws.10%29.aspx)
