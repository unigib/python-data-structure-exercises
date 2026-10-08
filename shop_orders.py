# This program analyses orders from a small online shop. The data is stored in
# shop_orders.json. Each order contains several line items, and each line item
# refers to a product by its SKU. Cancelled orders should not be included in
# sales totals.
#
# When the program is run, it should display a report about the shop's orders.

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

import argparse
import json
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


def build_report(products, orders):
    
    completed_orders = [
        order for order in orders if order['status'] == 'completed'
    ]

    customer_orders = defaultdict(int)
    customer_spending = defaultdict(Decimal)
    product_units = {sku: 0 for sku in products}
    product_revenue = {sku: Decimal('0') for sku in products}
    category_revenue = {
        product['category']: Decimal('0') for product in products.values()
    }
    date_revenue = defaultdict(Decimal)

    for order in completed_orders:
        customer = order['customer']
        customer_orders[customer] += 1
        order_revenue = Decimal('0')

        for item in order['items']:
            sku = item['sku']
            quantity = item['quantity']
            product = products[sku]
            revenue = Decimal(str(product['price'])) * quantity

            product_units[sku] += quantity
            product_revenue[sku] += revenue
            category_revenue[product['category']] += revenue
            order_revenue += revenue

        customer_spending[customer] += order_revenue
        date_revenue[order['date']] += order_revenue

    total_revenue = sum(date_revenue.values(), Decimal('0'))
    top_customer = (
        max(customer_spending, key=customer_spending.get)
        if customer_spending else None
    )
    top_product = (
        max(product_units, key=product_units.get)
        if product_units else None
    )
    top_category = (
        max(category_revenue, key=category_revenue.get)
        if category_revenue else None
    )

    summary = [
        'Completed orders: {}'.format(len(completed_orders)),
        'Total sales revenue: {:.2f}'.format(total_revenue),
        'Top customer: {} ({:.2f})'.format(
            top_customer or 'None',
            customer_spending[top_customer] if top_customer else Decimal('0'),
        ),
        'Most units sold: {} ({})'.format(
            products[top_product]['name'] if top_product else 'None',
            product_units[top_product] if top_product else 0,
        ),
        'Top category: {} ({:.2f})'.format(
            top_category or 'None',
            category_revenue[top_category] if top_category else Decimal('0'),
        ),
    ]

    customer_rows = [
        (customer, customer_orders[customer], '{:.2f}'.format(spending))
        for customer, spending in sorted(customer_spending.items())
    ]
    product_rows = [
        (
            products[sku]['name'],
            product_units[sku],
            '{:.2f}'.format(product_revenue[sku]),
        )
        for sku in sorted(
            products, key=lambda product_sku: product_revenue[product_sku],
            reverse=True,
        )
    ]
    date_rows = [
        (date, '{:.2f}'.format(revenue))
        for date, revenue in sorted(date_revenue.items())
    ]

    return summary, {
        'Customers': (('Customer', 'Orders', 'Total spending'), customer_rows),
        'Products': (('Product', 'Units sold', 'Revenue'), product_rows),
        'Revenue by date': (('Date', 'Revenue'), date_rows),
    }


def add_report_table(parent, headings, rows, ttk):
    table = ttk.Treeview(parent, columns=headings, show='headings')
    for heading in headings:
        table.heading(heading, text=heading)
        table.column(heading, anchor='w', width=180)

    scrollbar = ttk.Scrollbar(parent, orient='vertical', command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    table.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    for row in rows:
        table.insert('', 'end', values=row)


def display_report(summary, reports):
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title('Shop orders report')
    root.minsize(600, 420)

    summary_frame = ttk.LabelFrame(root, text='Shop summary', padding=12)
    summary_frame.pack(fill='x', padx=12, pady=(12, 6))
    for line in summary:
        ttk.Label(summary_frame, text=line).pack(anchor='w', pady=2)

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=12, pady=(6, 12))
    for title, (headings, rows) in reports.items():
        tab = ttk.Frame(notebook, padding=8)
        notebook.add(tab, text=title)
        add_report_table(tab, headings, rows, ttk)

    root.mainloop()


def print_report(summary, reports):
    print('Shop summary')
    for line in summary:
        print('  {}'.format(line))

    for title, (headings, rows) in reports.items():
        print('\n{}'.format(title))
        widths = [
            max(len(heading), *(len(str(row[index])) for row in rows))
            for index, heading in enumerate(headings)
        ]
        print('  ' + ' | '.join(
            heading.ljust(widths[index])
            for index, heading in enumerate(headings)
        ))
        print('  ' + '-+-'.join('-' * width for width in widths))
        for row in rows:
            print('  ' + ' | '.join(
                str(value).ljust(widths[index])
                for index, value in enumerate(row)
            ))


def main():
    parser = argparse.ArgumentParser(description='Display the shop orders report.')
    parser.add_argument(
        '--cli',
        action='store_true',
        help='print the report in the terminal instead of opening a Tkinter window',
    )
    args = parser.parse_args()

    data_file = Path(__file__).with_name('shop_orders.json')
    with data_file.open(encoding='utf-8') as file:
        data = json.load(file)

    summary, reports = build_report(data['products'], data['orders'])
    if args.cli:
        print_report(summary, reports)
    else:
        display_report(summary, reports)


if __name__ == '__main__':
    main()