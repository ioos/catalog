---
title: "Harvest Registry: THREDDS WAF Scripting"
layout: single
excerpt: "Harvest Registry: THREDDS WAF Scripting"
sitemap: false
permalink: /pages/registry/thredds_waf_scripting/
---
## Example Scripts ##
There are many possible techniques for generating a WAF of ISO 19115-2 metadata from a THREDDS server with the THREDDS ISO service enabled - for a list of useful tools,
refer to the [WAF Creation page]({{ site.url }}{{ site.baseurl }}/pages/registry/waf_creation).  For this reason,
and also due to the peculiarities of each THREDDS server configuration (aggregations, etc), a case-specific approach will be necessary for each situation.

However, starting from a working example can be helpful.  This page is a collection of example WAF generation scripts used by IOOS RAs to populate
their metadata WAFs for populating the Catalog.  Refer to the examples below and clone/download/modify the code from the [IOOS Catalog GitHub repo](https://github.com/ioos/catalog)
directly if it is useful.  

Please contribute any examples you'd like to share to help others in the process, refer to the
[Readme](https://github.com/ioos/catalog/blob/master/waf_generation_scripts) and submit a pull request with your organization's scripts.

### NERACOOS ###  
NERACOOS uses Python scripts that wrap the IOOS THREDDS Crawler directly to parse their [THREDDS Catalog](http://www.neracoos.org/thredds/UMO_SOS_historical_realtime_agg.xml)
of historical and real-time observations and output a WAF to feed into the Harvest Registry.  Also included is a second script without the THREDDS Crawler dependency that parses the catalog directly using the Python 'requests' library.  Details below:

- Source code: [https://github.com/ioos/catalog/tree/master/waf_generation_scripts/neracoos](https://github.com/ioos/catalog/tree/master/waf_generation_scripts/neracoos)
- Resulting WAF: [http://www.neracoos.org/WAF/UMaine/iso/](http://www.neracoos.org/WAF/UMaine/iso/)
