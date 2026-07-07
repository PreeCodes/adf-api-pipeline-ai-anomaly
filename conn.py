import pyodbc
conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=synapse-ukretail-workspace-ondemand.sql.azuresynapse.net;"
    "Database=UKRetailDWH;"
    "UID=sqladmin;PWD=Warmlite@123;"
    "Timeout=30;"
)
print("Connected!")