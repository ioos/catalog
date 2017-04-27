---
title: "IOOS Catalog Important Periods and Schedules"
layout: single
excerpt: "IOOS Catalog Important Periods and Schedules"
sitemap: false
permalink: /pages/architecture/schedule/
---
The IOOS Registry is responsible for downloading metadata from external
sources. The central WAF acts as a repository for all the metadata that the
registry downloads. CKAN will periodically download metadta from the central
WAF into it's internal database. CKAN will occasionally synchronize with
PyCSW's database.

It's helpful for providers to know the periods and intervals the system uses
for the various phases.

### Registry

The registry harvests all `published` harvest records at
18:00Z every day.

### CKAN

The IOOS Catalog will harvest after each registry harvest or
exactly 24h after the last harvest, whichever happens first.


### PyCSW

PyCSW is synchronized with CKAN every hour.


### Other

Cleanup scripts cleanup duplicate datasets that will sometimes be created if a
CKAN harvester fails to fully synchronize with the central WAF. These cleanup
scripts run once a week on Sundays at 00:00Z.
