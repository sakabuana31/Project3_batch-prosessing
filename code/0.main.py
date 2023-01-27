import psycopg2

#connect to postgresql
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
    print('Database connection success')
except:
    print('Database connection error')

#menggunakan kursor
cur = conn.cursor()
cur.execute('Select * from public.siswa')

#menampilkan hasil
all = cur.fetchall()
one = cur.fetchone()
conn.commit()

#print hasil dalam bentuk array list
for i in all:
    print(i)

#manipulasi data
for record in all:
    print(str(record[0]) + "-" + record[1])
