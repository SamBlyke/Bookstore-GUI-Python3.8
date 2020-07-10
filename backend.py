import sqlite3

def connect():
    conn=sqlite3.connect("books")
    cur=conn.cursor()
    #cur.execute("drop table book;")
    cur.execute("create table IF NOT EXISTS book (SrNo integer PRIMARY KEY, Title text,Author text, year integer,isbn integer);")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books")
    cur=conn.cursor()
    cur.execute("insert into book VALUES (NULL, ?,?,?,? );",(title,author,year,isbn))
    conn.commit()
    conn.close()

def viewall():
    conn=sqlite3.connect("books")
    cur=conn.cursor()
    cur.execute("select * from book;")
    row=cur.fetchall()
    conn.close()
    return row

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books")
    cur=conn.cursor()
    cur.execute("select * from book WHERE title=? OR author=? OR year=? OR isbn=?;",(title,author,year,isbn))
    row=cur.fetchall()
    conn.close()
    return row

def delete(srno):
    conn=sqlite3.connect("books")
    cur=conn.cursor()
    cur.execute("delete from book where SrNo=? OR author;",(srno,))
    conn.commit()
    conn.close()

def update(title,author,year,isbn,srno):
    conn=sqlite3.connect("books")
    cur=conn.cursor()
    cur.execute("update book set title=?,author=?,year=?,isbn=? where SrNo=?;",(title,author,year,isbn,srno))
    conn.commit()
    conn.close()

connect()
#insert("Brownssaasdad","Bitches Krisaddgaadtten",1956,75192)
print(search(author="Bitches Krisaddgaadtten"))
#print(viewall())
    
