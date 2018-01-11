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
    -waf waf
done

rm -r waf/ncml
rm -r waf/score
mv waf/iso/*.xml waf/
rm -r waf/iso
sed -i 's/bight_latest/bight_complete/g' waf/thredds_dodsC_latest_Bight_gcmplt.xml