---
title: "Harvest Registry Architecture"
layout: single
excerpt: "Harvest Registry Architecture"
sitemap: false
permalink: /pages/architecture/registry/
---

The IOOS Harvest Registry consists of a harvesting program, whihc kicks off the
individual harvester processes.  The harvester processes harvest from external
WAFs usually hosted by RAs and sync the contents to a local WAF.  Information
about the last sync time and any validation issues with ISO 19115 metadata
are written to a MongoDB instance.  This data is then presented to the user
through the harvest Registry webpage.

![Harvest Registry Architecture](/catalog/images/harvest_registry.svg "Harvest Registry")
