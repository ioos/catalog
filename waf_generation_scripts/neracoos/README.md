### NERACOOS WAF Scripting Examples ###

Examples for the NERACOOS THREDDS catalog at: <http://www.neracoos.org/thredds/UMO_SOS_historical_realtime_agg.xml>  
*should work for any TDS*

* `WAF_generator.py`: Example python script to harvest ISO metadata records from an ncISO enabled THREDDS server.

  Requires: IOOS [thredds_crawler:]( https://github.com/ioos/thredds_crawler)

  `usage: WAF_generator.py [-h] [waf_dir] [catalog_url]`

* `old_WAF_generator.py`: Example python script to harvest ISO metadata records from an ncISO enabled THREDDS server.  

  This one does not require: IOOS [thredds_crawler:]( https://github.com/ioos/thredds_crawler)

  ```
    usage: old_WAF_generator.py [-h] [-l]  
    -l, --local  Create WAF in current directory
  ```
