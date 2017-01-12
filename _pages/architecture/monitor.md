---
title: "Service Monitor Architecture"
layout: single
excerpt: "Service Monitor Architecture"
sitemap: false
permalink: /pages/architecture/monitor/
---

The IOOS service monitor consists of a Python application, a MongoDB server to
store data, and several Python worker processes to harvest data from the API on
the IOOS CKAN instance.  The service monitor application also performs run-time checking of individual services to ensure remote services are reachable, using the urls provided in the metadata.

![Service Monitor Architecture](/catalog/images/service_monitor_diagram.svg "Service Monitor Architecture")
