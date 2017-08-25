#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#檢查輸入資料格式

from .Data_AllByInput import ProfilefromGFinance

def Inputtest(company, ticker, datetime, speaker):

    Test_Result = ""
    
    while True:
        try:
            while ticker.isdigit() == True:
                if len(ticker) == 4 or len(ticker) == 6:
                    Test_Result = "AHJ"
                    baseurl = 'https://www.google.com/finance?q='
                    url = baseurl + ticker
                    language, description, title = ProfilefromGFinance(company, ticker, url)
                    return Test_Result, language, description, title
                    break
            
                else:
                    Test_Result = "AHJ Input Error"
                    return Test_Result, "N/A", "N/A", "N/A"
                    break 
    
            for i in ticker:
                if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                    Test_Result = "Success"
                    baseurl = 'https://www.google.com/finance?q='
                    url = baseurl + ticker
                    language, description, title = ProfilefromGFinance(company, ticker, url)
                    return Test_Result, language, description, title
                    break
                else:
                    Test_Result = "Input Error"
                    return Test_Result, "N/A", "N/A", "N/A" 
                    break
        
        except:
            Test_Result = "Input Error"
            return Test_Result, "N/A", "N/A", "N/A" 
            break
        
    
    
    
        
