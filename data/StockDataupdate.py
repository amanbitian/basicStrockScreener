from data.MysqlConnection import MysqlConnection
import pandas as pd
import yfinance as yf
class StockDataupdate():

    def get_tickers(self):
        mysql_conn = MysqlConnection()
        print(mysql_conn)
        # Get a MySQL connection
        connection = mysql_conn.get_mysql_connection()
        print("connection is established")
        if connection:
            query = "SELECT * FROM companies_ticker;"
            columns, results = mysql_conn.execute_query(connection, query)
            # print(type(results))
            # print(columns)
            # print(results)

            com_ticker= pd.DataFrame(results, columns=columns)
            # print(tickers.head(2))
            if connection:
                connection.close()
            return com_ticker

    def stock_data(self):
        tickers= StockDataupdate.get_tickers(self)
        print(tickers.sample(2))
        ticker_list=list(tickers['symbol'])
        # if connection_status['success']:
        #     try:
        #         # List of stock tickers
        #         stock_tickers = ['AAPL', 'GOOGL', 'MSFT']
        #
        #         for ticker in stock_tickers:
        #             # Create a table for each stock
        #             mysql_conn.create_stock_table(ticker)
        #
        #             # Fetch stock data
        #             stock_data = fetch_stock_data(ticker)
        #
        #             # Insert data into the corresponding table
        #             if stock_data is not None:
        #                 with mysql_conn.connection.cursor() as cursor:
        #                     for index, row in stock_data.iterrows():
        #                         insert_query = f"""
        #                             INSERT IGNORE INTO {ticker}_data
        #                             VALUES ('{row['Date']}', {row['Open']}, {row['High']},
        #                                     {row['Low']}, {row['Close']}, {row['Volume']},
        #                                     {row['Adj Close']});
        #                         """
        #                         cursor.execute(insert_query)

    def create_stock_table(self, company_name):
        try:
            # Create a cursor object
            mysql_conn = MysqlConnection()
            connection = mysql_conn.get_mysql_connection()
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
            mysql_conn.execute(create_table_query)
            print(f"Table {company_name}_data created successfully.")

        except mysql_conn.Error as err:
            print(f"Error: {err}")

    def fetch_stock_data(self, ticker):
        try:
            # Fetch historical stock data from Yahoo Finance
            stock_data = yf.download(ticker, start="2000-01-01", end="2023-01-24")

            # Convert the Date index to a column
            stock_data.reset_index(inplace=True)

            return stock_data

        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return None


st=StockDataupdate()
print("here")
# print(st.fetch_stock_data('360ONE.NS'))
# print(st.get_tickers()['company_name'])
cname=list(st.get_tickers()['company_name'])
for i in cname:
    st.create_stock_table(i)