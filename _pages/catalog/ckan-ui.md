---
title: "IOOS Data Catalog: CKAN User Interface"
layout: single
excerpt: "IOOS Data Catalog: CKAN User Interface"
sitemap: false
permalink: /pages/catalog/ckan-ui/
---
## CKAN User Interface ##


CKAN is a tool for making open data websites. (Think of a content management
system like WordPress - but for data, instead of pages and blog posts.) It
helps you manage and publish collections of data. It is used by national and
local governments, research institutions, and other organizations who collect a
lot of data.

Once your data is published, users can use its faceted search features to
browse and find the data they need, and preview it using maps, graphs and
tables - whether they are developers, journalists, researchers, NGOs, citizens,
or even your own staff.

*Above section Copyright 2009-2013 [Open Knowledge Foundation](http://okfn.org/).
Licensed under 
[Creative Commons Attribution ShareAlike (Unported) v3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).*

For more information about advanced uses of CKAN, please consult the 
[CKAN User Guide](http://docs.ckan.org/en/latest/user-guide.html).


### Basic UI Layout ###

The basic sections of the IOOS Catalog are:

- [Datasets](#datasets)
- [Organizations](#organizations)
- [Groups](#groups)
- [About](#about)

### Datasets ###

The datasets section is the primary interface to finding and discovering data
in the catalog. The interface includes a basic text search using the search box.

![Search Bar](/catalog/images/ckan-ui/search-bar.png)

The search bar works very intuitively by performing a full text search using
the contents of the field. The query is sent to the solr search-engine and all
matching documents are displayed in the order of most relevant. 

Relevance is determined by how closely the query matches key metadata like the
*title* and the *abstract*. If relevance being equal, the date-time of the
dataset determines the next precedence.


<img class="pull-right" alt="Map Filter" src="/catalog/images/ckan-ui/map-search.png" />

Search queries for datasets can be filtered to a geographic region using the
map interface on the left.

If you select the pencil icon in the upper right section of the map filter, the
map will expand and the user can draw a box. This box will be used to filter
out results that are not within the geographic region defined by the box the
user draws.


Below the search box are the listed results. Each of the matching results
determined by a text search, filtered by the map and ordered by the **Order
by** dropdown are presented below. Only 20 items are displayed at a time. At
the bottom of the results are the page numbers you can select to see more
results.

### Organizations ###

An organization in the IOOS Catalog represents an IOOS Regional Association or
National Partner. Each dataset collected by CKAN belongs to an organization.
This structure allows users to view, browse and find data belonging to a
particular entity.

The organizations page is laid out like cards, showing a small organization
logo or image, followed by a brief description and the total number of datasets
in the catalog belonging to that organization.

Clicking an organization in this view takes the user to a page almost identical
to the datasets page except the search results and contents are that belonging
to the organization.

Along the left-hand side of the page are statistics like the number of datasets
and quantity of repeating metadata tags found within the data. Clicking a tag
or format will filter the datasets to only those data containing the tag or
format. This is useful for finding all of the SOS data published by an
organization.

### Groups ### 

Groups represent the shared datasets to a particular project or team. The IOOS
Catalog does not currently have any defined groups.

### About ###

This section displays some basic information about the site and the technology
supporting the site.

CKAN is the world’s leading open-source data portal platform.

CKAN is a complete out-of-the-box software solution that makes data accessible
and usable – by providing tools to streamline publishing, sharing, finding and
using data (including storage of data and provision of robust data APIs). CKAN
is aimed at data publishers (national and regional governments, companies and
organizations) wanting to make their data open and available.

CKAN is used by governments and user groups worldwide and powers a variety of
official and community data portals including portals for local, national and
international government, such as the UK’s data.gov.uk and the European Union’s
publicdata.eu, the Brazilian dados.gov.br, Dutch and Netherland government
portals, as well as city and municipal sites in the US, UK, Argentina, Finland
and elsewhere.

CKAN: [http://ckan.org/](http://ckan.org/)

CKAN Tour: [http://ckan.org/tour/](http://ckan.org/tour/)

Features overview: [http://ckan.org/features/](http://ckan.org/features/)
