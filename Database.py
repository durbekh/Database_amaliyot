import sqlite3 as sql

with sql.connect("baza1.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
        )""")    
    
    cur.execute("""CREATE TABLE IF NOT EXISTS xaridlar(
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        product_name TEXT,
        price INTEGER
        )""") 
    
    cur.execute("""INSERT OR IGNORE INTO students(id , first_name , last_name , age) 
                VALUES (1, 'Abdulaziz','Palvonboyev', 15)""")
    cur.execute("""INSERT OR IGNORE INTO students(id , first_name , last_name , age) 
                VALUES (2, 'Shokirjon','Salayev', 17)""")
    
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , student_id , product_name , price)
                VALUES (1 ,1 ,'Uzum' , 10000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , student_id , product_name , price)
                VALUES (2 ,1 ,'Anor' , 40000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , student_id , product_name , price)
                VALUES (3 ,1 ,'Qazi', 150000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , student_id , product_name , price)
                VALUES (4 ,2 ,'Noutbuk' , 6500000)""")
    
con.commit()


