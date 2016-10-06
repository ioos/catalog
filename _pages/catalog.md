---
title: "IOOS Data Catalog Overview"
layout: single
excerpt: "IOOS Data Catalog Overview"
sitemap: false
permalink: /pages/catalog/
---
## IOOS Catalog Overview ##

<img class="pull-right" src="https://avatars3.githubusercontent.com/u/1630326?v=3&s=400" alt="CKAN Logo"/>

The IOOS Catalog leverages a powerful piece of software called CKAN. CKAN is a
powerful data management system that makes data accessible – by providing tools
to streamline publishing, sharing, finding and using data. CKAN is aimed at
data publishers (national and regional governments, companies and
organizations) wanting to make their data open and available.

One of the main missions for the IOOS Catalog is the ability to discover data
available from regional associations or national providers. 


### CKAN Internals ####

Once per day, CKAN will download all of the XML metadata documents from the
central WAF and update it's internal records. The download process is performed
by CKAN harvesters. Each harvester copies the XML contents into the CKAN
database and tries to read key metadata attributes from the XML documents. Some
of the key information CKAN needs is:

- Title
- Abstract
- Resources and Links
- Keywords and Metadata Tags
- Access Information
- Documentation
- Dataset Descriptions
- Geospatial Coverage
- Time Coverage
- Usage Constraints
- Lineage

Each dataset that CKAN copies is stored in two places. The main storage is a
[relational database](http://www.postgis.net/) and the other is a 
[search engine](https://lucene.apache.org/solr/). Because most of these
datasets have a coverage in space (for example, latitude and longitude), the
database and the search engine have the ability to index and find datasets
based on their location in space.

CKAN leverages [solr](https://lucene.apache.org/solr/) as the search engine.
Solr is based on [lucene](https://en.wikipedia.org/wiki/Lucene). It provides
advanced full-text-search capabilities, which allow users to find data by
describing what they are looking for to the search engine.

For more information on advanced searching within CKAN, please see the 
[API guide](http://docs.ckan.org/en/latest/api/index.html). 

