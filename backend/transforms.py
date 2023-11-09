import pandas as pd
import matplotlib.pyplot as plt
import db

#df = pd.read_csv('final_dataset.csv', parse_dates=['order_date'])

def insert_csv_to_db():
    df = pd.read_csv('final_dataset.csv', parse_dates=['order_date'], index_col=['order_date'])
    df = df.sort_index()
    db.construct_base_sales(df=df)

def complete_series(df: pd.DataFrame, product_name):
   
    p1 = df[df['product_name'] == product_name]

    all_dates = pd.date_range(start=p1['order_date'].min(), end=p1['order_date'].max(), freq='D')
    new_df = pd.DataFrame({'order_date': all_dates, 'quantity': 0})

    new_df['quantity'] = p1.groupby('order_date')['quantity'].sum().reindex(all_dates, fill_value=0).values

    return new_df['quantity']