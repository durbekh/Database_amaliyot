import sqlite3 as sql 
con = sql.connect("database1.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER,
    ism TEXT,
    fam TEXT,
    yosh INTEGER
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS xaridlar(
    id INTEGER,
    user_id INTEGER,
    nomi TEXT,
    narxi INTEGER
)""")

cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (1, 'Durbek' , 'Hayotbekov', 18)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (2, 'Farhotjon' , 'Abdullayev', 25)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (3, 'Anvar' , 'Jovliyev', 19)""")

cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (1, 1 ,'Olma', 25_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (2, 2 ,'Uzum', 30_000)""")


con.commit()
con.close()


