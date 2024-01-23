import pymysql


class MysqlConnection():
    def get_mysql_connection(self):
        try:
            # Replace these values with your actual database connection details
            db_config = {
                'host': 'localhost',
                'user': 'root',
                'password': '12345678',
                'database': 'stocks_data',
            }

            # Connect to MySQL
            connection = pymysql.connect(**db_config)

            return connection

        except pymysql.Error as err:
            print(f"Error: {err}")
            return None

    def execute_query(self, connection, query):
        try:
            # Create a cursor object
            with connection.cursor() as cursor:
                # Execute the query
                cursor.execute(query)

                # Fetch the results if needed
                results = cursor.fetchall()
                return results

        except pymysql.Error as err:
            print(f"Error: {err}")
            return None

        finally:
            # Close the connection
            if connection:
                connection.close()

# #try
# mysql_conn = MysqlConnection()
#
# # Get a MySQL connection
# connection = mysql_conn.get_mysql_connection()
#
# if connection:
#     query = "SELECT * FROM companies_ticker;"
#     results = mysql_conn.execute_query(connection, query)
#
#     if results:
#         for row in results:
#             print(row)
