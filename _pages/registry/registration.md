---
title: "Harvest Registry: Registration"
layout: single
excerpt: "Harvest Registry: Registration"
sitemap: false
permalink: /pages/registry/registration/
---
## Registering Data Sources for IOOS Catalog ##
The Harvest Registry is the entry point for publishing your data sets and services in the IOOS Catalog.  The Registry maintains a list of web-accessible folders (WAFs) from which the Catalog will harvest ISO 19115-2 compatible XML metadata records.  

The process to add your metadata is simple.  Request an account here: [https://registry.ioos.us/users/new](https://registry.ioos.us/users/new), providing your information as well as an organization affiliation.  Once your account and affiliation is approved, you'll be emailed a confirmation link to activate your account.

From the Registry interface, you can modify existing or add any new WAFs you want to publish to the Catalog for your organization.  Once a new WAF is registered, the CKAN Data Catalog will automatically trigger a harvest to read your metadata and add your datasets and services to its inventory.  Once this process is complete, your new data should be available in the Catalog (note, this process may take several minutes to complete, depending on the number of datasets in your organization as a whole).  

You can also manually trigger a re-harvest of an existing WAF directly from the Registry, if there have been changes made to the metadata in your WAF.  Just click on the 'Reharvest' button from the Data Source detail page.  By default, all WAFs are harvested on a daily basis by the Catalog.

### Current List of WAFs ###
A list of the WAFs and associated organizations currently in the Catalog can be found: [here](https://github.com/ioos/catalog/blob/master/doc/ioos_registry_wafs.csv)
