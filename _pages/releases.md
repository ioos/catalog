---
title: "Catalog Releases"
layout: single
excerpt: "Catalog Releases"
sitemap: false
permalink: /pages/releases/
---
Release history for the IOOS Catalog (GitHub releases and overall project version history).


## GitHub Releases ##
The IOOS Catalog is made up of several related components.  The two primary components are the CKAN data catalog, available
at the URL: [https://data.ioos.us/](https://data.ioos.us/), and the Harvest Registry, available at:
[https://registry.ioos.us/](https://registry.ioos.us).  

The Service Monitor is a downstream project that is primarily
meant for internal monitoring of service availability within the Catalog.  The Service Monitor is available here:
[http://monitor.ioos.us/](http://monitor.ioos.us/).

The GitHub release lists for each can be found below:

|**Project**|**Description**|**GitHub Repo**|**GitHub Releases**|
|--------|---------|---------|---------|
|**CKAN Data Catalog**|Web interface for public dataset access|[https://github.com/ioos/catalog-ckan](https://github.com/ioos/catalog-ckan)|[https://github.com/ioos/catalog-ckan/releases](https://github.com/ioos/catalog-ckan/releases)|
|**Harvest Registry**|Internal Web UI for IOOS data providers|[https://github.com/ioos/catalog-harvest-registry](https://github.com/ioos/catalog-harvest-registry)|[https://github.com/ioos/catalog-harvest-registry/releases](https://github.com/ioos/catalog-harvest-registry/releases)|
|**Service Monitor**|Monitoring and uptime site for Catalog services|[https://github.com/ioos/service-monitor](https://github.com/ioos/service-monitor)|[https://github.com/ioos/service-monitor/releases](https://github.com/ioos/service-monitor/releases)|


## Catalog Release Versions ##
The overall Catalog project version history, with major features included in each release.


### Version 1.4: April 11, 2019 ###
[[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/1.4.0)]

**IOOS Catalog Release 1.4: Search and Attribution Enhancements**

This release includes significant updates for search a filtering of datasets in the IOOS Catalog.  Below is a highlight list
of enhancements bundled in this release:

- Date/Time-based dataset search and filtering
- Integration with Google Dataset Search via Schema.org JSON-LD dataset metadata - via [CKAN DCAT extension](https://github.com/ckan/ckanext-dcat)
- Faceted filtering of IOOS 'Data Providers' as listed in ISO 19115 metadata
- Improved display of Global Change Master Directory (GCMD) keywords
- Upstream harvest of IOOS Catalog by [NOAA Catalog](https://data.noaa.gov/dataset) and [Data.gov](https://data.gov)
- Update to CKAN 2.8.2


**Details:**

Date/Time search: A major limitation of the standard CKAN software the IOOS Catalog uses is that there is no
fully-functional date/time dataset filtering capability.  Because IOOS' data is so time-specific, as part of this release
we developed custom code in the [ioos/catalog-ckan](https://github.com/ioos/catalog-ckan) repository that enabled a new
control in CKAN's [Datasets](https://data.ioos.us/datasets) view allowing users to enter specific ISO-8601
date/time strings or select from a calendar widget to filter by dataset start/end time, start time only, end time only, etc.

Google Dataset Search: a long-requested feature implemented in this release.  Via Schema.org/JSON-LD tagging of IOOS metadata -
enabled by the [ckanext-dcat](https://github.com/ckan/ckanext-dcat) extension - the full IOOS Catalog inventory is now
crawled, indexed, and searchable in Google Dataset Search.  Search for IOOS metadata in [Google Dataset Search](https://toolbox.google.com/datasetsearch/search?query=site%3Adata.ioos.us).

Data Provider filtering: IOOS' Regional Associations source data from a wide variety of partners/data providers.  This
information, when properly cited in dataset source XML metadata, can now be filtered in the IOOS Catalog via a new
'Data Provider' faceted filter control in the [Datasets](https://data.ioos.us/datasets) view.

GCMD Keywording: The IOOS Catalog now parses hierarchical GCMD keywords to allow display of only the actual term itself,
rather than the entire term hierarchy (as typically encoded in ISO XML metadata).  This aligns better with CF Standard Name
vocabularies, which are found in some IOOS datasets.  For example:

* `Oceans > Ocean Temperature > Water Temperature` becomes `Water Temperature` and
* `Oceans > Ocean Optics > Turbidity` becomes `Turbidity`



### Version 1.3: September 27, 2018 ###
[[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/1.3.0)]

IOOS Catalog Release 1.3 is primarily an update to CKAN version [2.8](https://ckan.org/2018/05/09/new-ckan-version-2-8-0-released-patch-versions-for-2-5-x-2-6-x-and-2-7-x-available/).  
Migrating IOOS’ Catalog to the newest CKAN version will allow new Catalog functionality,
such as time window filtering and more granular metadata filtering capabilities to be developed
by IOOS and more easily contributed back to the core CKAN code base.  This reduces the risk of
one-off feature development and should lessen future maintenance burden for IOOS going forward.

Other improvements bundled with this upgrade include:

- Resolution of issues with NDBC's SOS datasets, with implementation of ioos/sensorml2iso release [1.0.5](https://github.com/ioos/sensorml2iso/releases/tag/1.0.5) for SOS harvesting
- All ERDDAP URLs used within IOOS are properly harvested by CKAN/pycsw
- pycsw database synchronization improvements within CKAN

Many additional datasets have been added to the IOOS Catalog since the 1.2 release, including entire ERDDAP
catalogs for [SECOORA](https://data.ioos.us/organization/09cf7d59-3604-44f7-9c2c-5909d9705e40?res_format=ERDDAP),
[CeNCOOS](https://data.ioos.us/organization/091f805a-7ab6-4d1c-8b06-1214dd5c99c6?res_format=ERDDAP),
and [AOOS](https://data.ioos.us/organization/eb417ed8-8ef9-46e4-8cce-deec54104134?res_format=ERDDAP).

The associated Harvest Registry release [1.3.0](https://github.com/ioos/catalog-harvest-registry/releases/tag/1.3.0) includes the following updates:

- Additional required background information users must provide in order to request a Registry account
- Functionality improvements related to ERDDAP WAF harvesting and upstream CKAN harvesting controls
- Admin-level accounts automatically included in distribution emails for account registrations


### Version 1.2: January 12, 2018 ###
[[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/1.2.0)]

IOOS Catalog Release 1.2 includes a significant look and feel overhaul to make the Catalog resemble IOOS' other web
properties more closely.  It also includes project background and an FAQ section in the [About Page](https://data.ioos.us/about).
Other enhancements include: dataset-level feedback and the addition of IOOS datasets from [USGS](https://data.ioos.us/organization/usgs)
and the [US Navy](https://data.ioos.us/organization/us-navy), and others.  Internally, the IOOS Catalog now supports
CKAN's Google Analytics plugin to extract usage metrics.

The backend [Harvest Registry](https://registry.ioos.us/) tool added improved CS-W harvesting support to allow IOOS data
providers to register CS-W servers as data sources, as well as listing individual email address contact points for each
harvest source.  


### Version 1.1: April 28, 2017 ###   
[[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/v0.1.1)]

CKAN Data Catalog functionality improvements, including improved CS-W support, user feedback, and an API for programmatic
control of the dataset harvest process by data providers.  New features:

CKAN Data Catalog:

- Attribution of 'Operator' organizations in IOOS SOS services with metadata generated by the
[sensorml2iso](https://github.com/ioos/sensorml2iso) module
- IOOS data provider organization information included in the pycsw database and
[CS-W](https://data.ioos.us/csw?request=GetCapabilities&service=CSW&version=2.0.2) service
- User feedback now supported
   [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/catalog_feedback.png)
- pycsw service configuration supported in the CKAN UI

Harvest Registry:

- CKAN harvest job status reporting in the Registry UI
    [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/registry_ckan_job_status.png)
- Enhancement of the ['About'](https://registry.ioos.us/about) page to display total dataset count in Registry and
CKAN Data Catalog for comparison
    [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/registry_about_ckan_dataset_count.png)
- Registry [API]({{ site.url }}{{ site.baseurl }}/pages/registry/api) released to automate the Catalog harvesting process
- Better notification of harvest job status for users in the Registry UI


### Version 1.0: December 14, 2016 ###
Initial IOOS Data Catalog release including Harvest Registry integration for dataset publishing.  Initial high-level
features include:

CKAN Data Catalog:

- Initial CKAN UI enhancements and customizations for IOOS
- Proper parsing of service types by CKAN (OPeNDAP, ERDDAP-OPeNDAP, SOS, WMS)
    [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/catalog_dataset_formats.png)
- Tabbed dataset detail view (Access, Documentation, Description, ...)
    [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/catalog_dataset_details_tabs.png)

Harvest Registry:

- Harvest Registry deployed to manage IOOS data provider WAFs and harvesting
- Centralized data provider aggregated WAFs managed by Registry: [https://registry.ioos.us/waf/](https://registry.ioos.us/waf/)
- Automatic CKAN harvest initiation when a Registry reharvest is triggered (instant update ability for IOOS data providers)
- ISO 19115 validation and reporting for dataset error detection
    [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/registry_iso_validation_errors.png)
