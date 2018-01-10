#!/bin/bash
if [ ! -f ncISO-2.3.4.jar ]; then
    wget https://github.com/NOAA-PMEL/uafnciso/releases/download/2.3.4/ncISO-2.3.4.jar
fi

for full_cat in \
http://colossus.dl.stevens-tech.edu:8080/thredds/bight_latest.xml \
http://colossus.dl.stevens-tech.edu:8080/thredds/apex_latest.xml \
http://colossus.dl.stevens-tech.edu:8080/thredds/complete_latest.xml
do
  echo $full_cat
  java -Xms1024m -Xmx1024m -jar ncISO-2.3.4.jar \
    -ts ${full_cat} -num 100 -depth 20 -iso true \
    -waf /var/www/waf/Stevens
done

rm -r /var/www/waf/Stevens/ncml
rm -r /var/www/waf/Stevens/score
mv /var/www/waf/Stevens/iso/*.xml /var/www/waf/Stevens/
rm -r /var/www/waf/Stevens/iso