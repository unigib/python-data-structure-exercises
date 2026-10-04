# This program analyses orders from a small online shop. The data is stored in
# shop_orders.json. Each order contains several line items, and each line item
# refers to a product by its SKU. Cancelled orders should not be included in
# sales totals.
#
# When the program is run, it should display a report about the shop's orders.

import json
from pathlib import Path

data_file = Path(__file__).with_name('shop_orders.json')
with data_file.open(encoding='utf-8') as file:
    data = json.load(file)

products = data['products']
orders = data['orders']

print('There are {} products and {} orders'.format(len(products), len(orders)))


# TODO: Write code to answer the following questions, excluding cancelled orders:
# * How many orders were completed?
# * What was the total sales revenue?
# * Which customer spent the most?
# * Which product sold the most units?
# * Which product category earned the most revenue?

# TODO (extra):
# * Display a customer report showing order count and total spending.
# * Display a product report showing units sold and revenue, sorted by revenue.
# * Report the total revenue for each date with completed orders.