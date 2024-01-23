import pandas as pd


## We need to create 2 schema
indices= ["Nifty50", "Nifty200"]


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