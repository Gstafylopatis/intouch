import csv

fields = [
    'title', 'inventory', 'unit_price', 'purchase_price', 'last_update'
]

table = 'store_product'

insert_str = f'insert into {table}({", ".join(fields)})'

query = (f'{insert_str} \n' f'values')

with open('inventory.csv', 'r') as f:

    csv_reader = csv.reader(f, delimiter=';')
    next(csv_reader)

    for row in csv_reader:
        row = [f'"{item.replace(",", ".")}"' for item in row]
        row.append("date(now())")
        row_str = (f'({", ".join(row)}),\n')
        query = query + row_str

    query = query[:-2]  #Remove last comma and \n

with open('seed.sql', 'w') as f:
    f.write(query)