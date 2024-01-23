import requests
import sqlalchemy
import pymysql
import pandas as pd
import ssl
import yfinance as yf
import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Ignore SSL certificate verification (not recommended for production)
# ssl._create_default_https_context = ssl._create_unverified_context


## We need to create 3 schema
indices= ["Nifty50", "Nifty200"]

# print("db check")
# def schemacreator(index):
#     print("inside schema creator")
#     #                               db://user:password@hostport;/
#     engine=sqlalchemy.create_engine("mysql://root:Dec@2023@localhost3306:/")
#     engine.execute(sqlalchemy.schema.CreateSchema(index))
#     print(f"Connected to sql server and schema created {index}")
#
# for index in indices:
#     print(index)
#     schemacreator(index)

# ###
nifty50=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50', flavor='html5lib')[2]
#
nifty200= pd.read_html('https://en.wikipedia.org/wiki/NIFTY_500', flavor='html5lib')[2] #, skiprows=1)[2]

nifty50['Symbol']=nifty50['Symbol'] + ".NS"
nifty50_symbol= nifty50.Symbol.to_list()

# Set the second row as column names
new_header = nifty200.iloc[0]  # Get the second row as the new header
nifty200 = nifty200[1:]  # Skip the first row in the DataFrame
nifty200.columns = new_header
nifty200['Symbol']=nifty200['Symbol'] + ".NS"
nifty200_symbol= nifty200.Symbol.to_list()

# print(nifty200.info())
print(nifty200_symbol)
print(nifty200[['Company Name','Symbol']])

nifty200[['Company Name','Symbol']].to_csv('tickers_name_mapping.csv', index=False)