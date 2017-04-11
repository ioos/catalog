from thredds_iso_harvester.harvest import ThreddsIsoHarvester
from thredds_crawler.crawl import Crawl

#skip = Crawl.SKIPS + ['.*MATLAB.*']
skip = Crawl.SKIPS 
select = ['.*\_Best', '.*2009\_da.*']

# FWF
ThreddsIsoHarvester(catalog_url="http://tds.marine.rutgers.edu/thredds/roms/espresso/catalog.xml", 
    skip=skip, select=select,
    out_dir="/srv/iso/espresso")
