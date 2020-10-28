import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup
import csv

def scrapper(url):
        response = requests.get(url)

        soup = BeautifulSoup(response.text,"html.parser")
        table = soup.findAll('table',{"class":"processors"})[0] #Finds table with class named 'preprocessors'

        tr = table.findAll(['tr'])[0:]


        csvFile = open("cpudb2.csv",'a',newline='',encoding='utf-8')
        writer = csv.writer(csvFile) 
        try:   
                for cell in tr:
                    td = cell.find_all('td')
                    row = [i.text.replace('\n','') for i in td]
                    writer.writerow(row)      
        
        finally:   
            csvFile.close()


#List of urls for scrapping data
scrapper('https://www.techpowerup.com/cpu-specs/?mfgr=AMD&released=2019&mobile=No&server=No&sort=name')
scrapper('https://www.techpowerup.com/cpu-specs/?mfgr=AMD&released=2020&mobile=No&server=No&sort=name')
scrapper('https://www.techpowerup.com/cpu-specs/?mfgr=AMD&released=2018&mobile=No&server=No&sort=name')
scrapper('https://www.techpowerup.com/cpu-specs/?mfgr=AMD&released=2017&mobile=No&server=No&sort=name')

scrapper('https://www.techpowerup.com/cpu-specs/?mfgr=Intel&released=2020&mobile=No&server=No&sort=name')
scrapper('https://www.techpowerup.com/cpu-specs/?mfgr=Intel&released=2019&mobile=No&server=No&sort=name')
scrapper('https://www.techpowerup.com/cpu-specs/?mfgr=Intel&released=2018&mobile=No&server=No&sort=name')
scrapper('https://www.techpowerup.com/cpu-specs/?mfgr=Intel&released=2017&mobile=No&server=No&sort=name')

