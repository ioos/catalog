## Example scripts that work with the THREDDS ISO Harvester Docker container.

The advantage of using this approach is that you don't need python or a special python environment to harvest ISO metadata from THREDDSS catalogs.  You just need Docker installed.  The example scripts in this folder work with the [THREDDS ISO Harvester Docker Container](https://hub.docker.com/r/axiom/thredds_iso_harvester/).   You fire up the container from the command line with a script that contains your settings (which catalogs to point to, which files to skip, etc), the container does the work, and then quits, leaving you with a folder of ISO records.  

It's convenient to call the container with a simple script like this:
```
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
