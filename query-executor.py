import os
import pyodbc

# Database connection settings
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Set up the database connection
conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
try:
    conn = pyodbc.connect(conn_str)
    print("Database connection successful.")
except pyodbc.Error as e:
    print("Database connection failed:", e)
    exit()

# Function to execute SQL files
def execute_sql_file(file_path):
    try:
        with open(file_path, 'r') as sql_file:
            sql_script = sql_file.read()
            cursor = conn.cursor()
            cursor.execute(sql_script)
            cursor.commit()
            print(f"Executed SQL file {file_path}")
    except pyodbc.Error as e:
        print(f"Error executing SQL file {file_path}: {e}")

# Function to recursively search for SQL files
def execute_sql_files_in_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item.endswith('.sql'):
            execute_sql_file(item_path)
        elif os.path.isdir(item_path):
            execute_sql_files_in_folder(item_path)

# Execute SQL files in the specified directory and its subdirectories
execute_sql_files_in_folder('/path/to/sql/files/')