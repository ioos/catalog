---
title: "Harvest Registry Architecture"
layout: single
excerpt: "Harvest Registry Architecture"
sitemap: false
permalink: /pages/architecture/registry/
---

![Registry Architecture](/catalog/images/registry-architecture.png)

The Harvest registry is responsible for coordinating the downloading of
metadata from data providers and distributing that metadata to the IOOS
Catalog.

Users of the registry can create harvesting endpoints for their
organization(s). Daily, the harvest registry will download the XML documents in
that endpoint and store them in a _central WAF_. 

Once the metadata has been downloaded to the central WAF, CKAN will parse and
ingest all of the registry's metadata. The data is then present and available
for viewing within CKAN at [https://data.ioos.us/](https://data.ioos.us/).


