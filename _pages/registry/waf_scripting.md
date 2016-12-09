---
title: "Harvest Registry: WAF Scripting (THREDDS/ERDDAP)"
layout: single
excerpt: "Harvest Registry: WAF Scripting (THREDDS/ERDDAP)"
sitemap: false
permalink: /pages/registry/waf_scripting/
---
## THREDDS Example Scripts ##
There are many possible techniques for generating a WAF of ISO 19115-2 metadata from a
THREDDS server with the THREDDS ISO service enabled - for a list of useful tools, refer
to the [WAF Creation page]({{ site.url }}{{ site.baseurl }}/pages/registry/waf_creation).  For
this reason, and also due to the peculiarities of each THREDDS server configuration
(aggregations, etc), a case-specific approach will be necessary for each situation.

However, starting from a working example can be helpful.  This page is a collection of
example WAF generation scripts used by IOOS RAs to populate their metadata WAFs for
populating the Catalog.  Refer to the examples below and clone/download/modify the code
from the [IOOS Catalog GitHub repo](https://github.com/ioos/catalog)
directly if it is useful.  

Please contribute any examples you'd like to share to help others in the process, refer to the
[Readme](https://github.com/ioos/catalog/blob/master/waf_generation_scripts) and submit a pull request with your organization's scripts.

### NERACOOS ###  
NERACOOS uses Python scripts that wrap the IOOS THREDDS Crawler directly to parse their
[THREDDS Catalog](http://www.neracoos.org/thredds/UMO_SOS_historical_realtime_agg.xml)
of historical and real-time observations and output a WAF to feed into the Harvest
Registry.  Also included is a second script without the THREDDS Crawler dependency that
parses the catalog directly using the Python 'requests' library.  Details below:

- Source code: [https://github.com/ioos/catalog/tree/master/waf_generation_scripts/neracoos](https://github.com/ioos/catalog/tree/master/waf_generation_scripts/neracoos)
- Resulting WAF: [http://www.neracoos.org/WAF/UMaine/iso/](http://www.neracoos.org/WAF/UMaine/iso/)


## ERDDAP Example Scripts ##
ERDDAP includes a native WAF capability.  Appending the path /metadata/iso19115/xml/ to an
ERDDAP installation will display the WAF.  The Harvest Registry has been extended to be able to
harvest directly from an ERDDAP WAF.  In the 'New Harvest' dialog box select 'ERDDAP WAF' as the
Harvest Type to properly configure the harvest.

Below are some example ERDDAP native WAFs harvested by the Catalog:

- Glider DAC: [https://data.ioos.us/gliders/erddap/metadata/iso19115/xml/](https://data.ioos.us/gliders/erddap/metadata/iso19115/xml/)
- CO-OPS: [http://opendap.co-ops.nos.noaa.gov/erddap/metadata/iso19115/xml/](http://opendap.co-ops.nos.noaa.gov/erddap/metadata/iso19115/xml/)


### Glider DAC ###
If for some reason you prefer to not harvest from an ERDDAP WAF directly, the contents can always be
copied to a standard WAF via script.

The IOOS Glider DAC uses a simple Python script to scrape their ERDDAP server and output a metadata
WAF.  The script linked below includes code to query both THREDDS and ERDDAP servers, with a single
resulting WAF.  The ERDDAP approach could be applied for other use cases independent of the THREDDS
component.

- Source code: [https://github.com/ioos/glider-dac/blob/master/scripts/download_waf.py](https://github.com/ioos/glider-dac/blob/master/scripts/download_waf.py)
- Resulting WAF (also includes THREDDS content): [https://data.ioos.us/gliders/metadata/](https://data.ioos.us/gliders/metadata/)
