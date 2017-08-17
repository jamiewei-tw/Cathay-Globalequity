#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#所有資料手動輸入

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def ProfilefromGFinance(url): 

    head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}   
    response = requests.get(url, headers=head).content
    soup = BeautifulSoup(response, 'lxml')
    Description = soup.find('div', 'companySummary').contents[0]
    WholeTicker = soup.find('div', class_='appbar-snippet-secondary').span.text
    
    area, language = areacheck(WholeTicker)
           
    return(language, Description)

def areacheck(Ticker):
    Area = ''
    Language = ''
    location = Ticker.find(':')
    area = Ticker[1:location]
    US = ['NASDAQ','NYSE','AMEX']
    CH = ['SHE','SHA']
    
    
    if (area in US):
        Area = ' US'
        Language = 'English'
        
    elif (area in CH):
        Area = ' CH'
        Language = 'Mandarin'
        
    elif area == 'HKG':
        Area = ' HK'
        Language = 'Mandarin'
        
    elif area == 'TYO':
        Area = ' JP'
        Language = 'English'
        
    else:
        Area = ''
     
    return Area, Language

