#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#所有資料手動輸入

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def ProfilefromGFinance(Company, Ticker, url): 

    head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}   
    response = requests.get(url, headers=head).content
    soup = BeautifulSoup(response, 'lxml')
    Description = soup.find('div', 'companySummary').contents[0]
    WholeTicker = soup.find('div', class_='appbar-snippet-secondary').span.text
    
    area, language, title= areacheck(WholeTicker, Company, Ticker)
           
    return(language, Description, title)

def areacheck(wholeTicker, company, ticker):
    Area = ''
    Language = ''
    location = wholeTicker.find(':')
    area = wholeTicker[1:location]
    US = ['NASDAQ','NYSE','AMEX']
    CH = ['SHE','SHA']
    GR = ['ETR', 'FRA']
    
    
    if (area in US):
        Area = ' US'
        Language = 'English'
        title = company + '(' + ticker + Area + ')'
        
    elif (area in CH):
        Area = ' CH'
        Language = 'Mandarin'
        title = company + '(' + ticker + Area + ')'
        
    elif area == 'HKG':
        Area = ' HK'
        Language = 'Mandarin'
        title = company + '(' + ticker + Area + ')'
    
    elif area == 'TYO':
        Area = ' JP'
        Language = 'English'
        title = company + '(' + ticker + Area + ')'
                
    elif (area in GR):
        Area = ' GR'
        Language = 'English'
        title = company + '(' + ticker + Area + ')'

    elif area == 'LON':
        Area = ' LN'
        Language = 'English'
        title = company + '(' + ticker + Area + ')'
            
    elif area == 'ASX':
        Area = ' AU'
        Language = 'English'
        title = company + '(' + ticker + Area + ')'
        
    elif area == 'VTX':
        Area = ' VX'
        Language = 'English'
        title = company + '(' + ticker + Area + ')'

    elif area == 'KRX':
        Area = ' KRS'
        Language = 'Enlish'
        title = company + '(' + ticker + Area + ')'
        
    elif area == 'NSE':
        Area = ' IN'
        Language = 'English'
        title = company + '(' + ticker + Area + ')'

    else:
        Area = ''
        Language = 'English'
        title = company + '(' + ticker + ')'
     
    return Area, Language, title

