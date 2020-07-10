import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("create table IF NOT EXISTS %s (SrNo integer PRIMARY KEY, Title text,Author text, year integer,isbn integer);" %db)
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("insert into book VALUES (NULL, ?,?,?,? );",(title,author,year,isbn))
        self.conn.commit()

    def viewall(self):
        self.cur.execute("select * from book;")
        row=self.cur.fetchall()
        return row

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("select * from book WHERE title=? OR author=? OR year=? OR isbn=?;",(title,author,year,isbn))
        row=self.cur.fetchall()
        return row

    def remove(self,srno):
        self.cur.execute("delete from book where SrNo=? OR author;",(srno,))
        self.conn.commit()

    def update(self,title,author,year,isbn,srno):
        self.cur.execute("update book set title=?,author=?,year=?,isbn=? where SrNo=?;",(title,author,year,isbn,srno))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

database1=Database("books")
#insert("Brownssaasdad","Bitches Krisaddgaadtten",1956,75192)
#print(search(author="Bitches Krisaddgaadtten"))
#print(viewall())
        
