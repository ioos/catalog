from thredds_iso_harvester.harvest import ThreddsIsoHarvester
from thredds_crawler.crawl import Crawl

skip = Crawl.SKIPS 
select = ['.*']

ThreddsIsoHarvester(catalog_url="http://www.smast.umassd.edu:8080/thredds/forecasts.html", 
    skip=skip, select=select,
    out_dir="/srv/iso/necofs")
