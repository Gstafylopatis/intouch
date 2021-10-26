import csv

fields = [
    'name', 'tax_number', 'city', 'address', 'phone', 'phone2', 'email', 'doy',
    'created_on'
]

table = 'store_customer'

insert_str = f'insert into {table}({", ".join(fields)})'

query = (f'{insert_str} \n' f'values')

with open('clients.csv', 'r') as f:

    csv_reader = csv.reader(f, delimiter=';')
    next(csv_reader)

    for row in csv_reader:
        row = [f'"{item}"' for item in row]
        row.append("date(now())")
        row_str = (f'({", ".join(row)}),\n')
        query = query + row_str

    query = query[:-2]  #Remove last comma and \n

with open('seed.sql', 'w') as f:
    f.write(query)