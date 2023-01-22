import psycopg2
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
    print('success')
except:
    print('error')

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
cur.execute("INSERT INTO latihan_users VALUES (%s, %s, %s, %s, %s)", (1,'hello@mail.com', 'hello name', '111', '111-1212'))
conn.commit()
print("Create Table Success")
