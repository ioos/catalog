#!/bin/bash
# do_crawl harvest_comt2.py
docker run --rm -v $(pwd)/$1:/srv/harvest.py -v $(pwd)/iso:/srv/iso \
  axiom/thredds_iso_harvester
