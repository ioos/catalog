#! /usr/bin/env python
"""
Some utility functions for accessing and deciphering the THREDDS Catalog at:
  http://www.neracoos.org/thredds/sos_catalog.html
"""
import requests
from lxml import etree
from nspath_eval import nspath_eval
class datasetInfo:
  pass
#################################################
def get_catalog(cat_url):
  """
    Actually just gets the catalogRef's in the catalog.
  """

  try:
    req = requests.get(cat_url)
  except requests.exceptions.RequestException as e:    # This is the correct syntax
    print e
    exit(1)
  if req.status_code != requests.codes.ok:
    print "ERROR", req.status_code
    print "\t",req.reason
    print "\t",req.url
    return "ERROR"

  return req.content
####################################################
def parse_catalog_refs(xml_str):
  """
    parse catalog.xml and return references to sub catalogs.
  """
  root = etree.fromstring(xml_str)

  if not len(root):
    print "ERROR"
    exit(1)

  ns_map = root.nsmap
  # 
  ds_path = "//thredds:dataset"
  # should only be one of these
  ds =  root.xpath(ds_path, namespaces=ns_map)[0]
  ds_name = ds.get("name")

  cr_path = "//thredds:catalogRef"

  cr_list =  root.xpath(cr_path, namespaces=ns_map)

  results = []
  if len(cr_list) == 0:
    print "LEAF"
    return results

  for cr in cr_list:
    # simple attribute works.
    #print cr.get("name")
    #print cr.get(nspath_eval("xlink:href", ns_map))
    results.append(ds_name + "/" + cr.get(nspath_eval("xlink:href", ns_map)))

  return results
###########################################
def dict_parse_datasets(xml_str, tds_type):
  """
  This is deprecated.
  """
  results = {}
  root = etree.fromstring(xml_str)
  ns_map = root.nsmap
  # check a ns_map for a key of None, i.e.default namespace and set to arbitray prefix so we can use xpath
  # Search for k of None, delete and set a random prefix  to the original ns value
  for k,v in ns_map.items():
    if k == None:
      del ns_map[k]
      ns_map['tds'] = v
  svc_base = ''
  svc_path =  "/tds:catalog/tds:service/tds:service"
  services =  root.xpath(svc_path, namespaces=ns_map)
  for svc in services:
    if svc.get("name") == tds_type:
      svc_base = svc.get("base")
  buoy_path = "/tds:catalog/tds:dataset/tds:dataset"
  buoy_list =  root.xpath(buoy_path, namespaces=ns_map)
  for buoy in buoy_list:
    b_name =  buoy.get("name").split()[0]
    if not b_name in results:
      results[b_name] = []
    for data_set in buoy.xpath("tds:dataset", namespaces=ns_map):
      ds_id = data_set.get("ID")
      urlPath = data_set.get("urlPath")
      iso_url = svc_base + urlPath
      results[b_name].append(iso_url + '|' + ds_id )

  return results
###########################################
def parse_datasets(xml_str, tds_type):
  """
  """
  results = []
  root = etree.fromstring(xml_str)
  ns_map = root.nsmap
  # check a ns_map for a key of None, i.e.default namespace and set to arbitray prefix so we can use xpath
  # Search for k of None, delete and set a random prefix  to the original ns value
  for k,v in ns_map.items():
    if k == None:
      del ns_map[k]
      ns_map['tds'] = v
  svc_base = ''
  svc_path =  "/tds:catalog/tds:service/tds:service"
  services =  root.xpath(svc_path, namespaces=ns_map)
  for svc in services:
    if svc.get("name") == tds_type:
      svc_base = svc.get("base")
  buoy_path = "/tds:catalog/tds:dataset/tds:dataset"
  buoy_list =  root.xpath(buoy_path, namespaces=ns_map)
  for buoy in buoy_list:
    b_name =  buoy.get("name").split()[0]

    for data_set in buoy.xpath("tds:dataset", namespaces=ns_map):
      di = datasetInfo()
      di.buoy = b_name
      di.type = tds_type
      di.ds_id = data_set.get("ID")
      di.urlPath = data_set.get("urlPath")
      di.iso_url = svc_base + di.urlPath
      results.append(di)

  return results
##################################################
def run():
  # Note: this catalog has no catalogRef's
  tds_base = "http://www.neracoos.org"
  cat_url = tds_base + "/thredds/UMO_SOS_historical_realtime_agg.xml"
  xml = get_catalog(cat_url)
  if xml == 'ERROR':
    sys.stderr.write("ERROR: could not parse " + cat_url)
    exit()
  res = parse_datasets(xml, 'iso')
  unwanted_buoys = ['C02', 'J02', 'L01']
  for di in res:
    if di.buoy in unwanted_buoys:
      continue
    print di.buoy
    print "\t", di.ds_id
    print "\t", tds_base + di.iso_url
  
if __name__ == "__main__":
  run ()
