import sqlite3 as sql 
con = sql.connect("database1.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER,
    ism TEXT,
    fam TEXT,
    yosh INTEGER
)""")

cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (1, 'Durbek' , 'Hayotbekov', 18)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (2, 'Farhotjon' , 'Abdullayev', 25)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (3, 'Anvar' , 'Jovliyev', 19)""")

con.commit()
con.close()