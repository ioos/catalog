---
title: "CKAN Metadata Mapping"
layout: single
sitemap: false
permalink: /pages/catalog/mapping/
---

## CKAN Metadata Mapping ##

The following is a non-comprehensive list of metadata pulled from the ISO
documents. Each UI element of a CKAN's dataset page consists of metadata pulled
from the original ISO document.

For a comprehensive mapping, [click here](/catalog/doc/ISO-UI-Mapping.xlsx).

| UI Section | Section | ISO |
|---|---|---|
|Main|Title|gmd:title|
|Main|Abstract|gmd:abstract|
|Access|Online Access|gmd:CI_OnlineResource|
|Access|Online Access|gmd:CI_OnlineResource|
|Access|Distribution Formats|gmd:MD_Format/gmd:name|
|Access|Distribution Formats|gmd:MD_Format/gmd:version|
|Access|Dataset Point of Contact|gmd:individualName|
|Access|Dataset Point of Contact|gmd:organisationName|
|Access|Dataset Point of Contact|gmd:CI_Contact/gmd:phone|
|Access|Dataset Point of Contact|gmd:CI_Contact/gmd:address|
|Documentation|General Documentation|gmd:CI_OnlineResource/gmd:name|
|Documentation|General Documentation|gmd:CI_OnlineResource/gmd:linkage|
|Documentation|General Documentation|gmd:CI_OnlineResource/gmd:description|
|Documentation|Additional Documentation|gmd:CI_Citation/gmd:title|
|Description|Publisher|gmd:CI_ResponsibleParty|
|Description|Resource Provider|gmd:CI_ResponsibleParty|
|Description|Date(s)|gmd:CI_Citation/gmd:date|
|Description|Edition|gmd:CI_Citation/gmd:edition|
|Description|Data Presentation Form|gmd:CI_PresentationFormCode|
|Description|Dataset Progress Status|gmd:status|
|Coverage|Time Period|gmd:EX_TemporalExtent|
|Coverage|Geospatial|gmd:EX_GeographicBoundingBox|
|Keywords|All Sections Defined by Keywords Type|gmd:MD_Keywords|
|Constraints|Use/Access Constraints|gmd:MD_LegalConstraints|
|Constraints|Fees|gmd:fees|
|Lineage|Lineage Statement/Process|gmd:LI_Lineage|
