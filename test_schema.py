import json

def json_to_schema_dict():
    
    with open('test_data_dict.json', 'r') as f:
     json_data = json.load(f)
     
    try:
    # Assuming the JSON data is a list with a single dictionary 
        if isinstance(json_data, list) and len(json_data) == 1:
            data = json_data[0] 
            
        
        else:
            return {}  # Handle cases where the input is not as expected

        schema = {}
        for column in data.get('Columns', []): 
            schema[column['Name']] = {
            'DataType': column['DataType'],
            'Definition': column['Definition'],
            'SampleValues': column['SampleValues']
        }
        return schema
    except (KeyError, TypeError, IndexError) as e:
        print(f"Error processing JSON data: {e}")
        return {}



# Convert the JSON data to the desired dictionary format

if __name__ == "__main__":
    print(json_to_schema_dict())

# Print the resulting schema dictionary



# import pyodbc

# def connect_to_sql_server_with_aad(server, database):
#   """
#   Connects to a Microsoft SQL Server database using Azure Active Directory authentication.

#   Args:
#     server: The server name or IP address of the SQL Server instance.
#     database: The name of the database to connect to.

#   Returns:
#     A connection object to the SQL Server database.
#     Raises an exception if the connection fails.
#   """
#   try:
#     conn_str = (
#         r'DRIVER={ODBC Driver 17 for SQL Server};'
#         r'SERVER=tcp:' + server + ';'
#         r'PORT=1433;'
#         r'DATABASE=' + database + ';'
#         r'Authentication=ActiveDirectoryInteractive;' 
#     )
#     conn = pyodbc.connect(conn_str)
#     print("Connected to SQL Server using Azure Active Directory successfully.")
#     return conn
#   except pyodbc.Error as e:
#     print(f"Error connecting to SQL Server: {e}")
#     return None

# # Example Usage:
# server = 'syn-crowe-cmaa-nonprod-perfmd-002-ondemand.sql.azuresynapse.net'  # Replace with your server name
# database = 'db-cmaa-nonprod-perfmd-synlnk'  # Replace with your database name

# try:
#   conn = connect_to_sql_server_with_aad(server, database)
#   if conn:
#     # Perform SQL operations here (e.g., execute queries)
#     cursor = conn.cursor()
#     cursor.execute("SELECT TABLE_SCHEMA + '.' + TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'inventory%' and TABLE_SCHEMA LIKE 'gold'; ")  # Replace with your desired query
#     tables = cursor.fetchall()
#     db_schema = {}
#     for table in tables:
#       table_name = table[0]
    

#     conn.close() 
# except Exception as e:
#   print(f"An error occurred: {e}")