from thredds_iso_harvester.harvest import ThreddsIsoHarvester
from thredds_crawler.crawl import Crawl

skip = Crawl.SKIPS 
select = ['.*\/Best']

ThreddsIsoHarvester(catalog_url="http://thredds.ucar.edu/thredds/idd/forecastModels.xml", 
    skip=skip, select=select,
    out_dir="/srv/iso/unidata")
