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

#import csv file
with open('/home/sakabuana31/DigitalSkola/3.Project3_batch-prosessing/source/users_w_postal_code.csv') as f:
    #skip header
    next(f)
    cur.copy_from(f,'latihan_users',sep=',',columns=('email', 'name', 'phone', 'postal_code'))
conn.commit()

#menggunakan kursor
cur = conn.cursor()
cur.execute('Select * from public.latihan_users')

#menampilkan hasil
all = cur.fetchall()

#print hasil dalam bentuk array list
for i in all:
    print(i)