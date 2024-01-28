from data.MysqlConnection import MysqlConnection
import pandas as pd
import yfinance as yf
from datetime import datetime
class StockDataupdate():
    def get_tickers(self):
        mysql_conn = MysqlConnection()
        print(mysql_conn)
        # Get a MySQL connection
        connection = mysql_conn.get_mysql_connection()
        print("connection is established")
        if connection:
            query = "SELECT * FROM companies_ticker;"
            columns, results = mysql_conn.execute_query(connection, query,"fetch")
            # print(type(results))
            # print(columns)
            # print(results)

            com_ticker= pd.DataFrame(results, columns=columns)
            # print(tickers.head(2))
            if connection:
                pass
                # connection.close()
            return com_ticker

    def stock_data(self,stock_tickers,comp_name,connection):
        # tickers= StockDataupdate.get_tickers(self)
        # print(tickers.sample(2))
        # ticker_list=list(tickers['symbol'])
        ticker_list=stock_tickers
        # Get today's date
        end_date = str(datetime.now().date())

        # try:
        #
        if len(stock_tickers)==len(comp_name):
            for i in range(len(stock_tickers)):
                # Create a table for each stock
                # mysql_conn.create_stock_table(ticker)
                print(f"pushing data for {comp_name[i]}")
                # Fetch stock data
                stock_data = StockDataupdate.fetch_stock_data_from_yf(self,ticker_list[i],end_date)

                # Insert data into the corresponding table
                if stock_data is not None:
                    for index, row in stock_data.iterrows():
                        # print(row['Date'].date())
                        # print(type(row['Date'].date()))

                        insert_query = f"""
                            INSERT IGNORE INTO {comp_name[i]}_data
                            VALUES ('{row['Date'].date()}', {row['Open']}, {row['High']},
                                    {row['Low']}, {row['Close']}, {row['Volume']},
                                    {row['Adj Close']});
                        """
                        # cursor.execute(insert_query)
                        mysql_conn.execute_query(connection, insert_query, "insert")
        else:
            print("ticker len doesn't match comp_name")


    def create_stock_table(self, company_name, mysql_conn,connection):
        try:
            # Create a table for the stock data
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {company_name}_data (
                    Date DATE,
                    Open FLOAT,
                    High FLOAT,
                    Low FLOAT,
                    Close FLOAT,
                    Volume INT,
                    Adj_Close FLOAT,
                    PRIMARY KEY (Date)
                );
            """
            mysql_conn.execute_query(connection,create_table_query, "Create")
            print(f"Table {company_name}_data created successfully.")

        except Exception as err:
            print(f"Error: {err}")

    def fetch_stock_data_from_yf(self, ticker,end_date):
        try:
            # Fetch historical stock data from Yahoo Finance
            stock_data = yf.download(ticker, start="2000-01-01", end=end_date) #"2023-01-24")

            # Convert the Date index to a column
            stock_data.reset_index(inplace=True)

            return stock_data

        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return None


# Create a cursor object
mysql_conn = MysqlConnection()
connection = mysql_conn.get_mysql_connection()

st=StockDataupdate()
print("here")

cname=list(st.get_tickers()['company_name'])
stock_tickers=list(st.get_tickers()['symbol'])
### Cleaning org name to create sql table:
clean_name = []

for item in cname:
    # Replace spaces with underscores and remove periods
    transformed_item = item.replace(' ', '_').replace('.', '')
    clean_name.append(transformed_item)

print(len(clean_name))
print(len(stock_tickers))
# print(stock_tickers)
st.stock_data(stock_tickers,clean_name,connection)

### create a table
# for i in clean_name:
#     st.create_stock_table(i, mysql_conn,connection)

# st.fetch_stock_data_from_yf('360ONE.NS')
