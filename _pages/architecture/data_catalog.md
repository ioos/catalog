---
title: "Data Catalog Architecture"
layout: single
excerpt: "Data Catalog Architecture"
sitemap: false
permalink: /pages/architecture/data_catalog/
---

![Data Catalog Architecture](/catalog/images/data-catalog-architecture.png)

The data catalog consists of two distinct projects: CKAN and PyCSW. CKAN is a
open source data portal project and PyCSW is a python web interface that
implements OGC Catalog Service for the Web (CS-W).

CKAN has several components within the project:

 - [PostGIS](http://postgis.net/) Database for physically storing datasets, metadata, users, etc.
 - [Apache solr](https://lucene.apache.org/solr/) which acts as a search engine for the datasets and other metadata
 - [CKAN](https://ckan.org/) Front End which is a Python Web Service Gateway Interface (WSGI) which
   is built on pylons.
 - CKAN Plugins. CKAN is very modular and supports a plethora of plugins. The
   plugins we use:

   - [ckanext-spatial](https://ckanext-spatial.readthedocs.io/en/latest/): CKAN
     plugin to support geospatial data and be able to
     parse ISO-19139 XML documents implementing ISO-19115-2
   - [ckanext-harvest](https://github.com/ckan/ckanext-harvest): CKAN plugin to
     provide the framework for downloading
     and ingesting geospatial metadata from the IOOS Registry
   - [ckan-pycsw](http://docs.ckan.org/projects/ckanext-spatial/en/latest/csw.html):
     CKAN Plugin to synchronize CKAN data with PyCSW

