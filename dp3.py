import sqlite3 as sql

with sql.connect("baza.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
        )""")    
    
    cur.execute("""CREATE TABLE IF NOT EXISTS xaridlar(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_name TEXT,
        price INTEGER
        )""") 
    
    cur.execute("""INSERT OR IGNORE INTO users(id , first_name , last_name , age) 
                VALUES (1, 'Rasulbek','Xakimboyev', 15)""")
    cur.execute("""INSERT OR IGNORE INTO users(id , first_name , last_name , age) 
                VALUES (2 , 'Shokirjon' , 'Salayev' , 17)""")
    cur.execute("""INSERT OR IGNORE INTO users(id , first_name , last_name , age) 
                VALUES (3 , 'Farhotjon' , 'Abdullayev' , 16)""")
    cur.execute("""INSERT OR IGNORE INTO users(id , first_name , last_name , age) 
                VALUES (4 , 'Durbek' , 'Hayotbekov' , 16)""")
    cur.execute("""INSERT OR IGNORE INTO users(id , first_name , last_name , age) 
                VALUES (5 , 'Lobarxon' , 'Qodirova' , 16)""")
    cur.execute("""INSERT OR IGNORE INTO users(id , first_name , last_name , age) 
                VALUES (6 , 'Navrozbek' , 'Rajabov' , 16)""")
    cur.execute("""INSERT OR IGNORE INTO users(id , first_name , last_name , age) 
                VALUES (7 , 'Bekzod' , 'Lozayev' , 16)""")
    cur.execute("""INSERT OR IGNORE INTO users(id , first_name , last_name , age) 
                VALUES (8 , 'Shohjahon' , 'Baxtiyorov' , 16)""")
    
    
    
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (1 ,1 ,'Olma' , 10000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (2,2,'Uzum',25000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (3 ,3 ,'Olcha' , 15000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (4,4,'Gilos',35000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (5 ,5 ,'Banan' , 18000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (6,6,'Kitob',125000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (7 ,7 ,'Telefon' , 15_000_000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (8,8,'Kompyuter',25_000_000)""")
    con.commit()      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    