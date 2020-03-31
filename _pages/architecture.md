---
title: "IOOS Catalog Architecture"
layout: single
excerpt: "IOOS Catalog Architecture"
sitemap: false
permalink: /pages/architecture/
---

## High-Level Architecture ##
On a high-level, the Catalog consists of three complimentary components that, together, allow the IOOS Regional Associations and other IOOS data providers the ability to advertise
their datasets and associated DMAC data access services for public search and discovery and inclusion in IOOS National products (Environmental Data Server - [EDS](https://eds.ioos.us)
and [Sensor Map](https://sensors.ioos.us)).

The Catalog works by harvesting Web Accessible Folders containing ISO 19115-compliant metadata hosted by the RAs.  It is the responsibility of the RAs to publish metadata records
that accurately and completely describe their datasets and services, according to guidelines specified by IOOS (TBD).  

## System Diagram ##
<img src="{{ site.url }}{{ site.baseurl }}/images/Catalog-DMAC-Arch.png" style="padding: 15px; border: 2px solid #e5e5e5" alt="IOOS Catalog system diagram" title="IOOS Catalog system diagram"/>
<p style="text-align: center">  Figure 1. IOOS Catalog High Level Architecture </p>

## Catalog Components ##
The Catalog includes three major components:

### Harvest Registry ###
The Harvest Registry is a web application that provides an interface for data providers to register and manage WAFs of ISO 19115 metadata for harvest by the Catalog.  It includes software to
sync remote WAF and CS-W (coming soon) sources with consolidated, centralized WAFs per data provider organization.  

More information on the [Harvest Registry]({{ site.url }}{{ site.baseurl }}/pages/registry/).

The Harvest Registry is available at this URL: [https://registry.ioos.us/](https://registry.ioos.us/).

### Data Catalog ###
The Data Catalog is the search and discovery interface for the IOOS Catalog.  The Data Catalog is based on the [CKAN](http://ckan.org/) open data portal software.  CKAN harvests metadata
from the centralized data provider WAFs created and managed by the Harvest Registry, parses and validates the metadata content and extracts data access service endpoints for display to users.
CKAN also contains an embedded OGC Catalog Service-Web (CS-W) - provided by [pycsw](http://pycsw.org/) - that allows connection to other metadata catalogs including US Data.gov, GEOSS Portal, and others, as well as remote query from clients with CS-W search capabilities (such as [QGIS desktop GIS](http://www.qgis.org/) software with the MetaSearch plugin).

More information on the [Data Catalog]({{ site.url }}{{ site.baseurl }}/pages/catalog/).

The Data Catalog is available at this URL: [https://data.ioos.us/](https://data.ioos.us/).
