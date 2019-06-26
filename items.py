# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:52:01 2019

@author: Al_gou
"""

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinesechrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field() # Dict to store the url and corresponding character
    chr_parsed = scrapy.Field() # Str to store parsed characters
    chr_nodata = scrapy.Field() # Str to store no-result characters
