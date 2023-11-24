import  sqlite3

def create_connection(db_name):
    connection=sqlite3.connect(db_name)
    return connection

def create_table(connection, sql): 
    cursor = connection.cursor() 
    cursor.execute(sql)

sql_create_products = """ 
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY,
full_name VARCHAR(200) NOT NULL,
price DOUBLE (6, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER  NOT NULL  DEFAULT 0
);"""

connection = create_connection("hw.db")

create_table(connection, sql_create_products)
