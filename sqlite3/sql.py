import sqlite3
conn = sqlite3.connect("food_city.db")
cursor=conn.cursor()

cursor.execute("select * from items where id=5")
rows=cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("insert into items values (?,?,?)" ,(16,"milk chocalate",150))
conn.commit()

cursor.execute("select * from items")
rows=cursor.fetchall()

for row in rows:
    print(row)
