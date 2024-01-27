import pymysql
import os

class MysqlConnection():
    def get_mysql_connection(self):
        try:
            # Replace these values with your actual database connection details
            db_config = {
                'host': os.environ['host'],
                'user': os.environ['user'],
                'password': os.environ['password'],
                'database': os.environ['database'],
            }

            # Connect to MySQL
            connection = pymysql.connect(**db_config)
            print(connection)
            return connection
            # return {'success': True, 'message': 'Connected to MySQL'}

        except pymysql.Error as err:
            print(f"Error: {err}")
            return {'success': False, 'message': f"Connection error: {err}"}

    def execute_query(self, connection, query, type):
        try:
            # Create a cursor object
            with connection.cursor() as cursor:
                if type=="fetch":
                    # Execute the query
                    cursor.execute(query)
                    # Fetch the column names
                    columns = [desc[0] for desc in cursor.description]

                    # Fetch the results
                    results = cursor.fetchall()

                    return columns, results
                elif type=='Create':
                    cursor.execute(query)


        except pymysql.Error as err:
            print(f"Error: {err}")
            return None

        finally:
            pass
            # Close the connection
            # if connection:
            #     connection.close()

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
