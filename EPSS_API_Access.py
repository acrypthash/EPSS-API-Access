
import json
import requests
import pandas
import csv


#EPSS API URL
#url = 'https://api.first.org/data/v1/epss?envelope=true&pretty=true'
url = 'https://api.first.org/data/v1/epss?order=!epss'


#Datasets pulled from the API
headers = {
 'data'
 'Content-Type': 'application/json; charset=utf-8'
 }

#API Request
r = requests.get(url, headers=headers)

#panda stuff that was used for reviewing in terminal
files = r.json()
df = pandas.DataFrame(files)

#panada exports results to CSV
df.to_csv("EPSSresults.csv")
#print(df.to_string())


