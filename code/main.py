import psycopg2
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
    print('success')
except:
    print('error')

#menggunakan cursor
cur = conn.cursor()
cur.execute('Select')
