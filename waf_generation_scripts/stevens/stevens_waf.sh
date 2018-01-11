#!/bin/bash
if [ ! -f ~/ncISO-2.3.4.jar ]; then
wget https://github.com/NOAA-PMEL/uafnciso/releases/download/2.3.4/ncISO-2.3.4.jar -P ~/
fi

for full_cat in \
    http://colossus.dl.stevens-tech.edu:8080/thredds/bight_latest.xml \
    http://colossus.dl.stevens-tech.edu:8080/thredds/apex_latest.xml \
    http://colossus.dl.stevens-tech.edu:8080/thredds/complete_latest.xml
do
    echo $full_cat
    java -Xms1024m -Xmx1024m -jar ~/ncISO-2.3.4.jar \                                                                                                                                                 
        -ts ${full_cat} -num 100 -depth 20 -iso true \
        -waf /var/lib/docker/volumes/waf_data/_data/Stevens
done

rm -r /var/lib/docker/volumes/waf_data/_data/Stevens/ncml
rm -r /var/lib/docker/volumes/waf_data/_data/Stevens/score
mv /var/lib/docker/volumes/waf_data/_data/Stevens/iso/*.xml /var/lib/docker/volumes/waf_data/_data/Stevens/
rm -r /var/lib/docker/volumes/waf_data/_data/Stevens/iso
rm ncISO.log