from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import requests
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
print(page)
soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find("table")
temp_list = []
table_rows = star_table.find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]  
    temp_list.append(row)
names = []
distance = []
mass = []
radius = []
lum = []

for i in range(1,len(temp_list)):
    names.append(temp_list[i][1])
    lum.append(temp_list[i][7])
    radius.append(temp_list[i][6])
    mass.append(temp_list[i][5])
    distance.append(temp_list[i][3])

df2 = pd.DataFrame(list(zip(names,radius,lum,distance,mass)),columns = ['star name','distance','mass','luminosity','radius'])
print(df2)

df2.to_csv('bright_stars.csv')