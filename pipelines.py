# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:52:01 2019

@author: Al_gou
"""

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import time

class ChinesechrPipeline(object):
    def process_item(self, item, spider):  
        for k, v in item['url'].items():
            
            # Download png files to destination folder
            data = requests.get(k)
            with open('/Users/Al_gou/Desktop/Scraped/Pics/{}_{}.png'.\
                      format(k[8:].replace('/', '-'), v), 'wb') as f:
                f.write(data.content)
            
            # Write scraped urls to destination file
            with open('/Users/Al_gou/Desktop/Scraped/urls.csv', 'a') as f:
                f.write(k + '\t' + v + '\n')
        print('@ {}: {}-All pictures downloaded and CSV write completed.'.\
              format(time.ctime(), v))
        
        # Add parsed character to a destination file
        if item['chr_parsed']:
            with open('/Users/Al_gou/Desktop/Scraped/parsed.txt', 'a') as f:
                f.write(item['chr_parsed'])
            print('@ {}: {} added to parsed.txt'.format(time.ctime(), v))
        
        # Store character with no results to a destination file
        if item['chr_nodata']:
            with open('/Users/Al_gou/Desktop/Scraped/nodata.txt', 'a') as f:
                f.write(item['chr_nodata'])
            print('@ {}: {} added to nodata.txt'.format(time.ctime(), v))
            
        print('@ {}: {}-All completed!\n'.format(time.ctime(), v))

