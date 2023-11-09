import mysql.connector as db
import pandas as pd
from sqlalchemy import create_engine
from models import Sale

conn = db.connect(
    host='localhost',
    user='root',
    password=''
)
conn.reconnect()
engine = create_engine("mysql://root@localhost/storage_system")

cursor = conn.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS storage_system')

def get_all_sales():
    query = 'SELECT * FROM storage_system.ai_sales'
    df = pd.read_sql(query, conn)
    return df

def construct_base_sales(df : pd.DataFrame):
    df.to_sql(name='ai_sales', con=engine)

def get_one_product_sales(product_name : str):
    query = "SELECT * FROM storage_system.ai_sales WHERE product_name='" + product_name + "'"
    return pd.read_sql(query, con=engine)
   
def add_sale(s : Sale):
    query_raw = "INSERT INTO storage_system.ai_sales(order_date, product_name, quantity) VALUES('{order_date}', '{product_name}', {quantity})"
    query = query_raw.format(order_date = s.order_date, product_name=s.product_name, quantity=s.quantity)
    cursor.execute(query)
    conn.commit()