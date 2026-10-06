# %%
import sqlite3
import pandas as pd


# %%
# Create / connect to SQLite database
conn = sqlite3.connect("my_database.db")

print("Database created and connected successfully")


# %%
import os

os.getcwd()


# %%
os.listdir()


# %%
import os

db_path = os.path.abspath("my_database.db")
db_path


# %%
# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

conn.commit()
print("Table created successfully")


# %%
cursor.execute("""
INSERT INTO employees (name, department, salary)
VALUES ('Rahul', 'Analytics', 80000)
""")

cursor.execute("""
INSERT INTO employees (name, department, salary)
VALUES ('Anita', 'Finance', 90000)
""")

conn.commit()
print("Data inserted")


# %%
#Insert using Pandas DataFrame

# Create sample DataFrame
df = pd.DataFrame({
    "name": ["Amit", "Neha", "Suresh"],
    "department": ["IT", "HR", "Marketing"],
    "salary": [70000, 65000, 72000]
})

# Insert DataFrame into SQLite table
df.to_sql("employees", conn, if_exists="append", index=False)

print("Data inserted via DataFrame")


# %%
query = "SELECT * FROM employees"

df_read = pd.read_sql(query, conn)
df_read


# %%
conn.close()
print("Connection closed")


# %%
!pip install mysql-connector-python


# %%
import mysql.connector
import pandas as pd



# %%
conn = mysql.connector.connect(
    host="localhost",        # or 127.0.0.1
    user="root",             # your MySQL username
    password="Mayank12",# your MySQL password
    database="sakila"  # database you created in MySQL
)

print("Connected to MySQL successfully")


# %%
!pip uninstall mysql-connector-python -y
!pip install pymysql


# %%
import pymysql
import pandas as pd

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Mayank@12",
    database="sakila",
    port=3306
)

print("Connected to MySQL successfully")


# %%
query = "SELECT * FROM actor"
df = pd.read_sql(query, conn)
df


# %%




