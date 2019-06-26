# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:52:01 2019

@author: Al_gou
"""

import scrapy
import requests
from ChineseChr.items import ChinesechrItem
import time
import pandas as pd
import os


class ChrSpider(scrapy.Spider):
    name = 'chr'
    allowed_domains = ['sfzd.com']
    start_urls = ['http://www.sfzd.com/api/query.php']
    
    def parse(self, response):
        
        # Read the source file to get the character set to search
        with open('/Users/Al_gou/Desktop/Scraped/ChineseChar.txt', 'r') as f:
            charSet = f.read()
        
        # The site provides five fonts for each character
        fonts = ['楷', '行', '草', '隶', '篆']
        
        print('@ {} spider started. Crawling...'.format(time.ctime()))
        
        # Start the loop to iterate through the character set
        for char in charSet:
            
            # Initialize the scrapy item
            charItem = ChinesechrItem()
            charItem['url'] = {}
            charItem['chr_parsed'] = ''
            charItem['chr_nodata'] = ''
            
            # In case of interruption. Use a special set to decide where to begin
            if 'urls.csv' not in os.listdir('/Users/Al_gou/Desktop/Scraped/'):
                with open('/Users/Al_gou/Desktop/Scraped/urls.csv', 'w') as f:
                    f.write('')
            parsedSet = pd.read_csv('/Users/Al_gou/Desktop/Scraped/urls.csv',
                                    sep='\t',
                                    names=['url', 'char'])
            parsedSet = set(parsedSet.char)
            
            if char not in parsedSet:
                # Search each font for each character 
                for font in fonts:
                    # Construct the formdata
                    formdata = {'key': char, 
                                'font': font, 
                                'loaded': '0'}
                    # Use requests moduel to obtain the json of the query
                    res = requests.post(self.start_urls[0],formdata).json()
                    
                    # Stream data to scrapy item defined earlier
                    if len(res['list']) > 0:
                        for i in res['list']:
                            charItem['url'][i['_thumb_url']] = char
                        print('@ {}: {}-{} results yielded.'.\
                              format(time.ctime(),char, font))   
                    else:
                        print('@ {}: {}-{} no results yielded.'.\
                              format(time.ctime(), char, font))
            else:
                continue
            
            # In case of no data found, store these characters to a new field.
            if len(charItem['url']) > 0:
                charItem['chr_parsed'] = char
            else:
                charItem['chr_nodata'] = char
            
            yield charItem

                    
