#! /usr/bin/env python
"""
"""
import os
import argparse
import requests
# this will allow use of import unh_thredds_crawl
import neracoos_thredds_crawl as ntc

##################################################
def run():
  parser = argparse.ArgumentParser()
  parser.add_argument("-l", "--local", help=" Create WAF in current directory.", action="store_true")
  args = parser.parse_args()

  # WAF dir
  waf_base = '/home/www/htdocs/WAF'

  waf_dir = waf_base + '/UMaine/iso/'
  if args.local:
    waf_dir = 'WAF/'
    if not os.path.exists(waf_dir):
      os.makedirs(waf_dir)

  # Note: this catalog has no catalogRef's
  tds_base = "http://www.neracoos.org"
  cat_url = tds_base + "/thredds/UMO_SOS_historical_realtime_agg.xml"
  xml = ntc.get_catalog(cat_url)
  if xml == 'ERROR':
    sys.stderr.write("ERROR: could not parse " + cat_url)
    exit()
  res = ntc.parse_datasets(xml, 'iso')
  unwanted_buoys = []
  for di in res:
    if di.buoy in unwanted_buoys:
      continue
    waf_fn = di.ds_id + ".xml"
    full_waf_fn = waf_dir + waf_fn
    full_iso_url = tds_base + di.iso_url + "?catalog=" + cat_url + "&dataset=" + di.ds_id
    f = open(full_waf_fn, 'w')
    iso_xml = ntc.get_catalog(full_iso_url)
    f.write(iso_xml)
    f.close()
    print "Created:", full_waf_fn
    # for testing one file
    #exit()
  
if __name__ == "__main__":
  run ()
