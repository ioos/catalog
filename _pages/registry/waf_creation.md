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

See [http://www.unidata.ucar.edu/software/thredds/current/tds/reference/ncISO.html](http://www.unidata.ucar.edu/software/thredds/current/tds/reference/ncISO.html)
for details on how to enable ncISO.

Once enabled, export the file to the folder with the WAF, either through
manually using a web browser to save ISOs of interest or using a tool such as
`wget`: <br />

```
wget "http://dm1.caricoos.org/thredds/iso/buoys/RealTime/PR1/DSG_PR1.accelerometer2.realtime.nc?catalog=http%3A%2F%2Fdm1.caricoos.org%2Fthredds%2Fcatalog%2Fbuoys%2FRealTime%2FPR1%2Fcatalog.html&dataset=buoys%2FRealTime%2FPR1%2FDSG_PR1.accelerometer2.realtime.nc" -O "dest_dir/RealTime_FPR1_DSG_PR1.accelerometer2.realtime.xml"
```

### THREDDS Crawler Utilities ###
Some packages have been written to assist in crawling THREDDS Catalogs to extract datasets and associated metadata and service endpoints.  These may be useful in the WAF
generation process, as their function is primarily to traverse the THREDDS Catalog hierarchy and find particular datasets or aggregations.  From the primary
dataset endpoints in the THREDDS Catalog, WAF scripts can hit the ISO service endpoints to extract ISO 19115-2 metadata.

A few THREDDS crawler packages:

- IOOS THREDDS Crawler: [https://github.com/ioos/thredds_crawler](https://github.com/ioos/thredds_crawler)
- AXIOM THREDDS ISO Harvester: [https://github.com/axiom-data-science/thredds_iso_harvester](https://github.com/axiom-data-science/thredds_iso_harvester)
- Unidata Siphon: [https://github.com/Unidata/siphon](https://github.com/Unidata/siphon)

The IOOS THREDDS Crawler as well as the downstream THREDDS ISO Harvester script so far have been the primary tools used by IOOS data providers to create WAFs from THREDDS Catalogs.
See the [examples](#example-scripts) section below for more information.

At present, Siphon has not been leveraged for the WAF generation process for the IOOS Catalog, however it may be a suitable alternative for this purpose.  Any data providers that have
used Siphon for this purpose are asked to submit their scripts via [pull request to the Catalog](https://github.com/ioos/catalog) repo to share.  

### Example Scripts for THREDDS and ERDDAP ###
For more information and examples on scripting WAF generation from THREDDS, and also ERDDAP, see the information in the [WAF Scripting]({{ site.url }}{{ site.baseurl }}/pages/registry/waf_scripting)
page.  

## Hosting a WAF on a webserver. ##

These directions assume you have a folder on a filesystem with ISOs stored
within.

### Apache `.conf` files ###

In the .conf files, use the +Indexes directive

```
<Directory /usr/local/apache2/htdocs/listme>
  Options +Indexes
</Directory>
```

See: [https://wiki.apache.org/httpd/DirectoryListings](https://wiki.apache.org/httpd/DirectoryListings)

### Nginx ###

Inside of the `server` block, put the `autoindex on` inside the appropriate location block where the WAF directory is contained:

```
location /somedir {
       autoindex on;
}
```

See [http://nginx.org/en/docs/http/ngx_http_autoindex_module.html](http://nginx.org/en/docs/http/ngx_http_autoindex_module.html)

### IIS ###

[https://technet.microsoft.com/en-us/library/cc725840%28v=ws.10%29.aspx](https://technet.microsoft.com/en-us/library/cc725840%28v=ws.10%29.aspx)
