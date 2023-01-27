import psycopg2
import csv

#connect to postgresql
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
    print('Database connection success')
except:
    print('Database connection error')

#menggunakan kursor
cur = conn.cursor()

#create table
cur.execute("""
                CREATE TABLE IF NOT EXISTS latihan_import_csv(
                    id serial PRIMARY KEY,
                    email text,
                    name text,
                    phone text,
                    postal_code text
                )
    """
    )

#import csv file
with open('/home/sakabuana31/DigitalSkola/3.Project3_batch-prosessing/source/users_w_postal_code.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    #skip header
    next(csv_reader)
    for row in csv_reader:
        cur.execute("INSERT INTO latihan_users VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING", row)
conn.commit()
print("Create Table Success")