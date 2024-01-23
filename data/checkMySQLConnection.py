import os
import pandas as pd
import pymysql

def upload_csv_to_mysql(csv_file_path):
    try:
        # Replace these values with your actual database connection details
        db_config = {
            'host': os.environ['host'],
            'user': os.environ['user'],
            'password': os.environ['password'],
            'database': os.environ['database'],

        }

        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        # Connect to MySQL
        connection = pymysql.connect(**db_config)

        # Create a cursor object
        with connection.cursor() as cursor:
            # Create the 'stocks_data' schema if not present
            cursor.execute("CREATE DATABASE IF NOT EXISTS stocks_data;")
            cursor.execute("USE stocks_data;")

            # Create a 'companies' table if not present
            create_table_query = """
                CREATE TABLE IF NOT EXISTS companies_ticker (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    company_name VARCHAR(255),
                    symbol VARCHAR(40)
                );
            """
            cursor.execute(create_table_query)

            # Insert data into the 'companies' table
            for index, row in df.iterrows():
                insert_query = "INSERT INTO companies_ticker (company_name, symbol) VALUES (%s, %s);"
                cursor.execute(insert_query, (row['Company Name'], row['Symbol']))

        # Commit the changes and close the connection
        connection.commit()
        print("Data uploaded successfully.")

    except pymysql.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the connection
        if connection:
            connection.close()

# Provide the path to your CSV file
csv_file_path = 'tickers_name_mapping.csv'

# Call the function to upload data to MySQL
upload_csv_to_mysql(csv_file_path)
