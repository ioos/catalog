from thredds_iso_harvester.harvest import ThreddsIsoHarvester
from thredds_crawler.crawl import Crawl

#skip = Crawl.SKIPS + ['.*MATLAB.*']
skip = Crawl.SKIPS 
select = ['.*']

# FWF
ThreddsIsoHarvester(catalog_url="http://comt.sura.org/thredds/comt_1_archive_summary.html", 
    skip=skip, select=select,
    out_dir="/srv/iso/comt")
