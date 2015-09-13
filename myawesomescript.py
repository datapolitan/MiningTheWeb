import requests
import json
import pandas as pd

print 'NYC OpenData Catalogue'

opendata_catalog = requests.get('https://data.cityofnewyork.us/resource/tdsx-cvye.json')
opendata_catalog_df = pd.io.json.json_normalize(opendata_catalog.json())

# print opendata_catalog_df.columns
interest_col = ['name.description', 'keywords', 'description', 'category', 'attribution.description']
print opendata_catalog_df[interst_col]
