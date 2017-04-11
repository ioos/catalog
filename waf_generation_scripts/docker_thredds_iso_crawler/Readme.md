This folder contains example scripts that work with the `axiom/thredds_iso_harvester` Docker container.

It's convenient to create a small bash script that takes the example script as argument.

For example:
do_crawl.sh harvest_necofs.py
```
where `do_crawl.sh` is:
```
#!/bin/bash
# Usage: do_crawl <harvest>.py
docker run --rm -v $(pwd)/$1:/srv/harvest.py -v $(pwd)/iso:/srv/iso  axiom/thredds_iso_harvester
```
and `harvest_necofs.py` is:
```
from thredds_iso_harvester.harvest import ThreddsIsoHarvester
from thredds_crawler.crawl import Crawl

skip = Crawl.SKIPS
select = ['.*']

ThreddsIsoHarvester(catalog_url="http://www.smast.umassd.edu:8080/thredds/forecasts.html",
    skip=skip, select=select,
    out_dir="/srv/iso/necofs")
```

The files that get produced looks like this:
```
$ls ./iso/necofs

gom3_nocache.iso.xml     
massbay_nocache.iso.xml   
necofs_met.iso.xml
hampton_nocache.iso.xml
necofs_gom3_wave.iso.xml
```
