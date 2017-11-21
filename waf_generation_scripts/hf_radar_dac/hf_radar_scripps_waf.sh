#!/bin/bash

python WAF_generator.py --waf_dir=/var/www/html/mwengren/hf_radar_dac --catalog_url=http://hfrnet.ucsd.edu/thredds/HFRADAR_USWC_hourly_RTV.xml
python WAF_generator.py --waf_dir=/var/www/html/mwengren/hf_radar_dac --catalog_url=http://hfrnet.ucsd.edu/thredds/HFRADAR_USEGC_hourly_RTV.xml
python WAF_generator.py --waf_dir=/var/www/html/mwengren/hf_radar_dac --catalog_url=http://hfrnet.ucsd.edu/thredds/HFRADAR_USHI_hourly_RTV.xml
python WAF_generator.py --waf_dir=/var/www/html/mwengren/hf_radar_dac --catalog_url=http://hfrnet.ucsd.edu/thredds/HFRADAR_AKNS_hourly_RTV.xml
python WAF_generator.py --waf_dir=/var/www/html/mwengren/hf_radar_dac --catalog_url=http://hfrnet.ucsd.edu/thredds/HFRADAR_PRVI_hourly_RTV.xml
