---
title: "Data Catalog Architecture"
layout: single
excerpt: "Data Catalog Architecture"
sitemap: false
permalink: /pages/architecture/data_catalog/
---

The IOOS Data Catalog is composed of several main portions:

- A server running the main CKAN instance.

- A public facing web server running Nginx to serve static and dynamic content
to end users.

- Several worker processes which harvest from the IOOS Registry WAF.

- A central WAF from which CKAN harvests.

- A PyCSW instance which syncs with the contents of the CKAN database.

- A Solr instance to allow full-text search and geospatial searching of uploaded
data.

- A PostgreSQL instance with databases for CKAN and PyCSW contents.

Figure 1 shows a diagram with the architecture of the IOOS Catalog

![Figure 1](/catalog/images/catalog_architecture.svg "Catalog Architecture") 
