#! /usr/bin/env python
"""
Example using thredds_crawler to generate a WAF for the NERACOOS THREDDS catalog at:
http://www.neracoos.org/thredds/UMO_SOS_historical_realtime_agg.xml
Requires: https://github.com/asascience-open/thredds_crawler
"""
import os
import requests
import argparse
from thredds_crawler.crawl import Crawl
#################################################
def get_catalog(cat_url):
  try:
    req = requests.get(cat_url)
  except requests.exceptions.RequestException as e:
    print(e)
    return False
  if req.status_code != requests.codes.ok:
    print("ERROR", req.status_code)
    print("\t",req.reason)
    print("\t",req.url)
    return False

  return req.content
####################################################

if __name__ == "__main__":
  default_cat_url = "http://www.neracoos.org/thredds/UMO_SOS_historical_realtime_agg.xml"
  parser = argparse.ArgumentParser()
  parser.add_argument("--waf_dir", help="WAF directory. Defalt local WAF/", nargs='?', default="WAF/")
  parser.add_argument("--catalog_url", help="Catalog URL. Default: " + default_cat_url, nargs='?', default=default_cat_url)

  args = parser.parse_args()
  print(args)

  cat_url = args.catalog_url
  waf_dir = args.waf_dir
  if not waf_dir.endswith("/"):
    waf_dir = waf_dir + "/"
  if not os.path.exists(waf_dir):
   os.makedirs(waf_dir)

  # Based on the NERACOOS UMaine TDS dataset ID's which are uniform.
  # E.g. SOS_DSG_B01_MET_Historic_Realtime_Agg
  # SOS_DSG_B01_MET, Crawl has a regex search which could be used to get a single buoy.
  unwanted_buoys = []
  cat = Crawl(cat_url)
  for ds in cat.datasets:
    #buoy = ds.id.split("_")[2]
    #if buoy in unwanted_buoys:
    #  continue
    url = [s.get("url") for s in ds.services if s.get("service").lower() == "iso"][0]
    #print buoy, url
    print("Debug - id: {id}\nds: {ds}".format(id=ds.id, ds=ds))
    #for service in ds.services:
    #    print("Service URL: {url}".format(url=service.get("url")))
    iso_xml = get_catalog(url)
    if iso_xml:
        #print("iso_xml: {xml}".format(xml=iso_xml))
        if len(ds.id.split("/")) > 1:
            ds.id = ds.id.replace("/", "_")
        waf_fn = waf_dir + ds.id + ".xml"
        f = open(waf_fn, 'wb')
        f.write(iso_xml)
        f.close()
