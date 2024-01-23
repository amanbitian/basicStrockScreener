from data.MysqlConnection import MysqlConnection

mysql_conn = MysqlConnection()

# Get a MySQL connection
connection = mysql_conn.get_mysql_connection()
print("connection is established")
if connection:
    query = "SELECT * FROM companies_ticker;"
    results = mysql_conn.execute_query(connection, query)

    if results:
        for row in results:
            print(row)
