---
title: "Catalog Releases"
layout: single
excerpt: "Catalog Releases"
sitemap: false
permalink: /pages/releases/
---
Release history for the IOOS Catalog (GitHub releases and overall project version history).


## GitHub Releases ##
The IOOS Catalog is made up of two primary components: the CKAN data catalog, available at the URL: [https://data.ioos.us/](https://data.ioos.us/), and the Harvest Registry, available at: [https://registry.ioos.us/](https://registry.ioos.us).

The GitHub release lists for each can be found below:

|**Project**|**Description**|**GitHub Repo**|**GitHub Releases**|
|--------|---------|---------|---------|
|**CKAN Data Catalog**|Web interface for public dataset access|[https://github.com/ioos/catalog-ckan](https://github.com/ioos/catalog-ckan)|[https://github.com/ioos/catalog-ckan/releases](https://github.com/ioos/catalog-ckan/releases)|
|**Harvest Registry**|Internal Web UI for IOOS data providers|[https://github.com/ioos/catalog-harvest-registry](https://github.com/ioos/catalog-harvest-registry)|[https://github.com/ioos/catalog-harvest-registry/releases](https://github.com/ioos/catalog-harvest-registry/releases)|



## Catalog Release History ##
The overall Catalog project release history, with information on the major features included in each release.


### Release 1.6: IOOS Metadata Profile 1.2/IOOS National Products Integration ###
**March 22, 2021**  [[catalog-ckan release tag](https://github.com/ioos/catalog-ckan/releases/tag/1.6)] [[catalog-docker-base release tag](https://github.com/ioos/catalog-docker-base/releases/tag/1.6)]

**IOOS Metadata Profile 1.2**: IOOS Catalog Release 1.6 adds support for [IOOS Metadata Profile 1.2](https://ioos.github.io/ioos-metadata/ioos-metadata-profile-v1-2.html) attribution for datasets harvested from ERDDAP.  This will improve query and filter capabilties for upstream IOOS National Products - such as the [IOOS Sensor Map](https://sensors.ioos.us/) and [IOOS Model Viewer](https://eds.ioos.us/) - allowing identification of Regional Association datasets suitable for ingest and display according to IOOS' dataset guidance.  See an example of CeNCOOS' San Luis Bay - Cal Poly MET station showing attribution from Metadata Profile 1.2 - [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/catalog_ioos_1.2_metadata.png).

<!-- ![IOOS Metadata Profile 1.2 example](/catalog/images/releases/catalog_ioos_1.2_metadata.png){:style="width: 425px; display: block; margin-left: auto; margin-right: auto;"} -->

IOOS Metadata Profile 1.2 attributes can be used as filter queries using special search syntax of Solr, the CKAN query engine.  The following is an example query to select datasets that include `gts_ingest=true` and exclude `ioos_ingest=false` attributes, which might be useful for identifying ERDDAP datasets suitable for harvest by IOOS National Products or to publish to the WMO GTS:
- CKAN UI: [https://data.ioos.us/dataset?q=gts_ingest:true+-ioos_ingest:false](https://data.ioos.us/dataset?q=gts_ingest%3Atrue+-ioos_ingest%3Afalse)
- CKAN API: [https://data.ioos.us/api/3/action/package_search?fq=gts_ingest:true -ioos_ingest:false&start=0](https://data.ioos.us/api/3/action/package_search?fq=gts_ingest:true%20-ioos_ingest:false&start=0) 

**CKAN Query Enhancements**: IOOS Catalog at Release 1.6 now provides the capability to: 

- filter for datasets that include [ERDDAP 'griddap' services](https://data.ioos.us/dataset?res_format=ERDDAP-GridDAP) (in addition to ERDDAP 'tabledap')
- filter by [depth in meters](https://data.ioos.us/dataset?q=&sort=score+desc%2C+metadata_modified+desc&ext_timerange_start=&ext_timerange_end=&ext_min_depth=50&ext_max_depth=100) for datasets that include depth metadata

**IOOS Centralized WAF**: Improvements were made to the IOOS centralized WAF [https://data.ioos.us/waf](https://data.ioos.us/waf) and CS-W service [https://data.ioos.us/csw](https://data.ioos.us/csw) in Release 1.6 so both resources properly delete records that data providers have removed from the Catalog.  Both now mirror Catalog content exactly, which makes them suitable for harvest by external catalog services such as [NOAA's OneStop](https://data.noaa.gov/onestop/) and [Data.gov](https://data.gov/).  The centralized IOOS WAF was created in Release 1.5 to allow OneStop to harvest IOOS' metadata as part of the NOAA transition to OneStop as the primary NOAA metadata catalog.

This release also includes minor styling and UI improvements to improve the look and feel and consistency of IOOS' overall [ioos.us](https://ioos.us) websites.

### Release 1.5: Schema.org Metadata Enhancements and Improved Filter/Query ###
**April 3, 2020**  [[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/1.4.2)]

Improvements to the IOOS Catalog for Release 1.5 center around findability of IOOS’ datasets (i.e. search and discovery) as described in the [FAIR data management principles](https://doi.org/10.1038/sdata.2016.18).  

Specifically, this release includes the following enhancements:

**Schema.org Metadata**: this release enhances the Schema.org-compliant JSON-LD metadata the IOOS Catalog provides for indexing by Google Dataset Search, which was recently released from beta (see Google's [blog post announcement](https://www.blog.google/products/search/discovering-millions-datasets-web/)).  The Catalog now provides a dataset’s geographic bounding box, time period coverage, download formats, and dataset license in the structure [recommended by Google](https://developers.google.com/search/docs/data-types/dataset).  This added metadata allows for improved search and filtering of IOOS Catalog content in Google’s dataset tool.  A few examples follow:

- PacIOOS ROMS Hawaii [search results](https://datasetsearch.research.google.com/search?query=site%3A%20data.ioos.us%20ROMS%20Hawaii)
- IOOS Glider DAC Silbo Challenger ‘silbo-20190717T1917’ glider [search results](https://datasetsearch.research.google.com/search?query=site%3A%20data.ioos.us%20silbo-20190717T1917)
- NERACOOS Buoy A01 Directional Waves [search results](https://datasetsearch.research.google.com/search?query=site%3A%20data.ioos.us%20A01%20Directional%20Waves)
- OOI Endurance Array (served by IOOS Glider DAC) [search results](https://datasetsearch.research.google.com/search?query=site%3Adata.ioos.us%20ce_383-20200220T2031)


**CF Standard Names and NASA Global Change Master Directory (GCMD) keyword functionality**: The Catalog now parses keywords from well-known science vocabularies, specifically the CF Standard Names and NASA Global Change Master Directory (GCMD), to present them in distinct UI elements and to provide the ability for users to filter datasets according to specific terms in each.  Previously, all dataset keywords had been aggregated together, making filtering more challenging.   

This IOOS Glider DAC Spray Glider [dataset](https://data.ioos.us/dataset/sp047-20180508t1650dfb1f) highlights the separate presentation of CF Standard Names and hierarchical GCMD keywords.  

**Filtering Improvements** New filters specific to both CF Standard Names and GCMD Keywords have been added.  The two URLs below show two ways to search PacIOOS’ collection of datasets for any that are: 1) available via ERDDAP, 2) contain the CF Standard Name ‘sea_water_turbidity’, and 3) the GCMD keyword for Ocean Chemistry > Oxygen (which returns 7 datasets at the time of writing):  

- PacIOOS [dataset query](https://data.ioos.us/dataset?res_format=ERDDAP-TableDAP&organization=pacioos&cf_standard_names=sea_water_turbidity&gcmd_keywords=EARTH+SCIENCE+%3E+OCEANS+%3E+OCEAN+CHEMISTRY+%3E+OXYGEN) displayed in IOOS Catalog user interface
- PacIOOS [dataset query](https://data.ioos.us/api/3/action/package_search?q=organization:pacioos%20and%20res_format:ERDDAP-TableDAP%20and%20cf_standard_names:sea_water_turbidity%20and%20gcmd_keywords:%22EARTH%20SCIENCE%20%3E%20OCEANS%20%3E%20OCEAN%20CHEMISTRY%20%3E%20OXYGEN%22&start=0) via CKAN API (JSON)  

For advanced users, the ability to efficiently narrow results in the IOOS Catalog using these new filters adds a new level of functionality.  When combined with existing filters (e.g. geospatial, time/date coverage, data provider, and free-text search), targeting IOOS data specific to a use case is easier than ever.


**Centralized WAF**:  IOOS Catalog was also updated to provide a centralized WAF of all IOOS metadata records, enabling easier harvest into NOAA metadata management systems (e.g. NOAA OneStop).  The centralized WAF has content identical to the Catalog’s OGC CS-W service, and is available at: [https://data.ioos.us/waf](https://data.ioos.us/waf).  The new WAF ensures IOOS’ data is available in NOAA’s enterprise data catalogs, the US Government-wide Data.gov platform, and any other open data aggregator that would like to include IOOS' open data.

NOAA OneStop, NOAA's new flagship open data portal, now routinely ingests IOOS data from the centralized WAF.  Users can find IOOS’ data on OneStop here: [https://data.noaa.gov/onestop](https://data.noaa.gov/onestop).


**Additional Features/Behind the Scenes**: Beyond the search and filter enhancements, the IOOS Catalog now includes a better basemap for the bounding box draw tool, as well as proper display of point datasets in the map preview window.   

Harvesting job management was improved, additional service security and monitoring was added, and the overall Catalog server architecture was made more robust as part of this release to better support its growing user base.


### Release 1.4: Search and Attribution Enhancements ###
**April 11, 2019** [[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/1.4.0)]

This release includes significant updates for search and filtering of datasets in the IOOS Catalog, and new connections to external data catalogs.  Below is a highlight list of enhancements bundled in this release:

- Date/Time-based dataset search and filtering
- Faceted filtering of IOOS 'Data Providers' as listed in ISO 19115 metadata
- Google Dataset Search integration via Schema.org JSON-LD dataset metadata
- Upstream harvest of IOOS Catalog by [NOAA Catalog](https://data.noaa.gov/dataset) and [Data.gov](https://data.gov)
- Improved display of NASA Global Change Master Directory (GCMD) keywords
- Update to CKAN 2.8.2

**Date/Time search**: A major limitation of the out-of-the-box CKAN software the IOOS Catalog uses is that there is no fully-functional date/time dataset filtering capability.  Because IOOS' data is so time-specific, we added in the [ioos/catalog-ckan](https://github.com/ioos/catalog-ckan) repository custom code allowing users to filter datasets via a new 'Date/Time Selection' control in CKAN's [Datasets](https://data.ioos.us/dataset) view.  The control allows users to enter specific ISO-8601 date/time strings or select from a calendar widget to filter datasets. Options for filtering include specifying both start/end time, start time only, and end time only.

**Data Provider filtering**: IOOS' Regional Associations source data from a wide variety of partners/data providers.  This information - when properly attributed in THREDDS/ERDDAP/SOS services and corresponding XML metadata fed to the Catalog - can now be filtered in the IOOS Catalog via a new 'Data Provider' faceted filter control in the [Datasets](https://data.ioos.us/dataset) view.

**Google Dataset Search**: a long-requested feature implemented in this release.  Via Schema.org/JSON-LD tagging of IOOS metadata - enabled by the [ckanext-dcat extension](https://github.com/ckan/ckanext-dcat) - the full IOOS Catalog inventory is now crawled, indexed, and searchable in Google Dataset Search.  Future work in this area will include enhancing the Schema.org metadata content available for Google to crawl.  

* Search [Google Dataset Search](https://toolbox.google.com/datasetsearch/search?query=site%3Adata.ioos.us) for IOOS datasets.     

**NOAA Catalog/Data.gov harvest**: All of the IOOS Catalog's datasets can now be found in the NOAA Catalog and Data.gov sites.  This is a long term goal finally achieved after many technical and non-technical barriers.  Harvest by these upstream sites is accomplished via the Catalog's [CS-W](https://data.ioos.us/csw) service.

**Improved GCMD Keywording display**: The IOOS Catalog now parses hierarchical GCMD keywords to display only the actual term itself, rather than the entire term hierarchy (as typically encoded in ISO XML metadata).  This aligns better with single-term CF Standard Name vocabularies, which are also found in some IOOS dataset metadata keywording.  For example:

* `Oceans > Ocean Temperature > Water Temperature` becomes `Oceans`, `Ocean Temperature`, `Water Temperature` and
* `Oceans > Ocean Optics > Turbidity` becomes `Oceans`, `Ocean Optics`, `Turbidity`


### Release 1.3: CKAN 2.8 and ERDDAP Harvest Support ###
**September 27, 2018** [[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/1.3.0)]

IOOS Catalog Release 1.3 is primarily an update to CKAN version [2.8](https://ckan.org/2018/05/09/new-ckan-version-2-8-0-released-patch-versions-for-2-5-x-2-6-x-and-2-7-x-available/).  Migrating IOOS’ Catalog to the newest CKAN version will allow new Catalog functionality, such as time window filtering and more granular metadata filtering capabilities to be developed by IOOS and more easily contributed back to the core CKAN code base.  This reduces the risk of one-off feature development and should lessen future maintenance burden for IOOS going forward.

Other improvements bundled with this upgrade include:

- Resolution of issues with NDBC's SOS datasets, with implementation of ioos/sensorml2iso release [1.0.5](https://github.com/ioos/sensorml2iso/releases/tag/1.0.5) for SOS harvesting
- All ERDDAP URLs used within IOOS are properly harvested by CKAN/pycsw
- pycsw database synchronization improvements within CKAN

Many additional datasets have been added to the IOOS Catalog since the 1.2 release, including entire ERDDAP catalogs for [SECOORA](https://data.ioos.us/organization/09cf7d59-3604-44f7-9c2c-5909d9705e40?res_format=ERDDAP), [CeNCOOS](https://data.ioos.us/organization/091f805a-7ab6-4d1c-8b06-1214dd5c99c6?res_format=ERDDAP), and [AOOS](https://data.ioos.us/organization/eb417ed8-8ef9-46e4-8cce-deec54104134?res_format=ERDDAP).

The associated Harvest Registry release [1.3.0](https://github.com/ioos/catalog-harvest-registry/releases/tag/1.3.0) includes the following updates:

- Additional required background information users must provide in order to request a Registry account
- Functionality improvements related to ERDDAP WAF harvesting and upstream CKAN harvesting controls
- Admin-level accounts automatically included in distribution emails for account registrations


### Release 1.2: IOOS.us Styling and CS-W Harvest Support ###
**January 12, 2018** [[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/1.2.0)]

IOOS Catalog Release 1.2 includes a significant look and feel overhaul to make the Catalog resemble IOOS' other web properties more closely.  It also includes project background and an FAQ section in the [About Page](https://data.ioos.us/about). Other enhancements include: dataset-level feedback and the addition of IOOS datasets from [USGS](https://data.ioos.us/organization/usgs) and the [US Navy](https://data.ioos.us/organization/us-navy), and others.  Internally, the IOOS Catalog now supports CKAN's Google Analytics plugin to extract usage metrics.

The backend [Harvest Registry](https://registry.ioos.us/) tool added improved CS-W harvesting support to allow IOOS data providers to register CS-W servers as data sources, as well as listing individual email address contact points for each harvest source.  


### Release 1.1 Harvest Registry/CKAN Integration & Data Provider Attribution ###   
**April 28, 2017** [[GitHub release tag](https://github.com/ioos/catalog-ckan/releases/tag/v0.1.1)]

CKAN Data Catalog functionality improvements, including improved CS-W support, user feedback, and an API for programmatic control of the dataset harvest process by data providers.  New features:

CKAN Data Catalog:

- Attribution of 'Operator' organizations in IOOS SOS services with metadata generated by the [sensorml2iso](https://github.com/ioos/sensorml2iso) module
- IOOS data provider organization information included in the pycsw database and [CS-W](https://data.ioos.us/csw?request=GetCapabilities&service=CSW&version=2.0.2) service
- User feedback now supported [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/catalog_feedback.png)
- pycsw service configuration supported in the CKAN UI

Harvest Registry:

- CKAN harvest job status reporting in the Registry UI [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/registry_ckan_job_status.png)
- Enhancement of the ['About'](https://registry.ioos.us/about) page to display total dataset count in Registry and CKAN Data Catalog for comparison [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/registry_about_ckan_dataset_count.png)
- Registry [API]({{ site.url }}{{ site.baseurl }}/pages/registry/api) released to automate the Catalog harvesting process
- Better notification of harvest job status for users in the Registry UI


### Release 1.0: Initial IOOS Catalog Release ###
**December 14, 2016**

Initial IOOS Data Catalog release including Harvest Registry integration for dataset publishing.  Initial high-level features include:

CKAN Data Catalog:

- Initial CKAN UI enhancements and customizations for IOOS
- Proper parsing of service types by CKAN (OPeNDAP, ERDDAP-OPeNDAP, SOS, WMS) [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/catalog_dataset_formats.png)
- Tabbed dataset detail view (Access, Documentation, Description, ...) [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/catalog_dataset_details_tabs.png)

Harvest Registry:

- Harvest Registry deployed to manage IOOS data provider WAFs and harvesting
- Centralized data provider aggregated WAFs managed by Registry: [https://registry.ioos.us/waf/](https://registry.ioos.us/waf/)
- Automatic CKAN harvest initiation when a Registry reharvest is triggered (instant update ability for IOOS data providers)
- ISO 19115 validation and reporting for dataset error detection
    [[screenshot]]({{ site.url }}{{ site.baseurl }}/images/releases/registry_iso_validation_errors.png)
