import requests
import json
import pandas as pd

print 'NYC OpenData Catalogue'

opendata_catalog = requests.get('https://data.cityofnewyork.us/resource/tdsx-cvye.json')
opendata_catalog_df = pd.io.json.json_normalize(opendata_catalog.json())

# print opendata_catalog_df.columns
interest_col = ['name.description', 'keywords', 'description', 'category', 'attribution.description']
print opendata_catalog_df[interest_col]

print 'After writing the above script'
print 'I saw that I am supposed to do a quick intro of myself'
print 'Hi all, my name is Doh'
print 'Currently working for a Socia Media analytics company called Brandwatch as a data analyst'
print 'After learning a thing or two about python, pandas and matplotlib,'
print 'I wanted to learn more about Data Visualization, particularly how to map things'
print 'So here I am!'
