import psycopg2

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
                CREATE TABLE IF NOT EXISTS latihan_users(
                    id serial PRIMARY KEY,
                    email text,
                    name text,
                    phone text,
                    postal_code text
                )
    """
    )

#input manual data
cur.execute("INSERT INTO latihan_users VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
            (2,'hai@mael.com', 'hai mail', '121', '121-2212'))
conn.commit()
print("Create Table Success")

#menggunakan kursor
cur = conn.cursor()
cur.execute('Select * from public.latihan_users')

#menampilkan hasil
all = cur.fetchall()

#print hasil dalam bentuk array list
for i in all:
    print(i)