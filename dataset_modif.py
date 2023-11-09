import pandas as pd
dataset = pd.read_csv('datasets/olist_order_items_dataset.csv')

new_dataset = dataset[dataset['product_id'].isin([
    'aca2eb7d00ea1a7b8ebd4e68314663af',
    '99a4788cb24856965c36a24e339b6058',
    '422879e10f46682990de24d770e7f83d',
    '389d119b48cf3043d311335e499d9c6b',
    '368c6c730842d78016ad823897a372db'
    ])]


new_dataset["product_id"] = new_dataset["product_id"].replace(
    [
        'aca2eb7d00ea1a7b8ebd4e68314663af',
        '99a4788cb24856965c36a24e339b6058',
        '422879e10f46682990de24d770e7f83d',
        '389d119b48cf3043d311335e499d9c6b',
        '368c6c730842d78016ad823897a372db',
    ],
    [
        'Dell XPS 13 Laptop',
        'Logitech MX Master 3 Mouse',
        'Bose QuietComfort 35 II Headphones',
        'Sony Alpha a7 III Camera',
        'ASUS RT-AX86U Wi-Fi Router',
    ],
)



new_dataset = new_dataset.rename(columns={'shipping_limit_date': 'order_date'})
new_dataset = new_dataset.rename(columns={'product_id': 'product_name'})

new_dataset['order_date'] = pd.to_datetime(new_dataset['order_date'])
new_dataset['order_date'] = new_dataset['order_date'].dt.strftime('%m/%d/%Y')
new_dataset = new_dataset.groupby(['order_date', 'product_name']).size().reset_index(name='quantity')

new_dataset.to_csv('analysis/final_dataset.csv')


"""
new_dataset['last_3_days_quantity'] = new_dataset.groupby('product_name')['quantity'].rolling(window=3).sum().reset_index(0, drop=True)
new_dataset['last_7_days_quantity'] = new_dataset.groupby('product_name')['quantity'].rolling(window=7).sum().reset_index(0, drop=True)

"""