#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#所有資料手動輸入

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def ProfilefromGFinance(ticker, datetime, speaker, dialin, passcode, url): 

    head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}   
    response = requests.get(url, headers=head).content
    soup = BeautifulSoup(response, 'lxml')
    Summary = soup.find('div', 'companySummary').contents[0]
    CompanyName = soup.find('div', class_='appbar-snippet-primary').span.text
    WholeTicker = soup.find('div', class_='appbar-snippet-secondary').span.text
    
    area, language = areacheck(WholeTicker)
    
    R_ticker = '(' + ticker + area + ')'
    content(R_ticker, datetime, speaker, language, dialin, passcode, CompanyName, Summary)

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
    
    
    
def content(Stock, datetime, speaker, language, dialin, passcode, CompanyName, Description):
    Company = CompanyName + Stock 
    W.write('Date & Time:' + datetime + '\n')
    W.write('Company: ' + Company + '\n')
    W.write('Spearker: ' + speaker + '\n')
    W.write('Language: ' + language + '\n')
    W.write('Dial In: ' + dialin + '\n')
    W.write('Passcode: ' + passcode + '\n')
    W.write(Description)
    

    
if __name__ == '__main__':
    ticker = input("Ticker: ")
    datetime = input("Date & Time: ")
    speaker = input("Speaker: ")
    dialin = input("Dial in: ")
    passcode = input("Passcode: ")
    Filename = ticker + '.txt'
    W = open(ticker, "w")
    baseurl = 'https://www.google.com/finance?q='
    url = baseurl + ticker
    ProfilefromGFinance(ticker, datetime, speaker, dialin, passcode, url)
   
