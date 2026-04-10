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
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (4, 'Rasulbek' , 'Hakimboyev', 20)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (5, 'Bexruz' , 'Jumabayev', 26)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (6, 'Navroz' , 'Rajabov', 29)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (7, 'Sulaymon' , 'Qurbonov', 28)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (8, 'Javohir' , 'Qutlimurodov', 35)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (9, 'Xusniddin' , 'Qurbonvoyev', 19)""")
cur.execute("""INSERT INTO users(id , ism , fam , yosh) VALUES (10, 'Sarvar' , 'Salimov', 13)""")

cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (1, 1 ,'Olma', 25_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (2, 2 ,'Uzum', 30_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (3, 3 ,'Banan', 35_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (4, 4 ,'Nok', 32_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (5, 5 ,'Orik', 29_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (6, 6 ,'Shaftoli', 38_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (7, 7 ,'Olhori', 23_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (8, 8 ,'Olcha', 33_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (9, 9 ,'Gilos', 29_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (10, 10 ,'Mango', 50_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (11, 1 ,'Batareya', 5_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (12, 2 ,'Televizor', 3_300_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (13, 3 ,'Kompyuter', 8_250_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (14, 4 ,'Kozoynak', 30_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (15, 5 ,'Kozgu', 250_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (16, 6 ,'Sumka', 300_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (17, 7 ,'Taqinchoq', 15_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (18, 8 ,'Uzuk', 3_300_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (19, 9 ,'Kamera', 230_000)""")
cur.execute("""INSERT INTO xaridlar(id , user_id, nomi , narxi) VALUES (20, 10 ,'Kitob', 36_000)""")


con.commit()
con.close()

