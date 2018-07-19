import sqlite3


def connectD(dbname,table):
	conn = sqlite3.connect(dbname+".sqlite")
	curs = conn.cursor()
	curs.execute("create table if not exists "+table+"(title TEXT, author TEXT, year TEXT, isbn TEXT)")
	conn.commit()
	curs.close()
	conn.close()
	
def insertD(dbname,table,title,author,year,isbn):
	conn = sqlite3.connect(dbname + ".sqlite")
	curs = conn.cursor()
	curs.execute("insert into "+table+" values(?,?,?,?)",(title,author,year,isbn))
	conn.commit()
	curs.close()
	conn.close()

def fetchD(dbname,table):
	conn = sqlite3.connect(dbname + ".sqlite")
	curs = conn.cursor()
	curs.execute("select * from "+table)
	rows = curs.fetchall()
	curs.close()
	conn.close()
	return rows
	
def updateD(dbname,table,title,author,year,isbn):
	conn = sqlite3.connect(dbname + ".sqlite")
	curs = conn.cursor()
	curs.execute("update " + table + " set title = ?, author = ?, year = ? where isbn = '"+isbn+"'",(title,author,year))
	conn.commit()
	curs.close()
	conn.close()

def deleteDRow(dbname,table,title,author,year,isbn):
	conn = sqlite3.connect(dbname + ".sqlite")
	curs = conn.cursor()
	curs.execute("delete from "+table+" where title= ? or author = ? or year = ? or isbn = ?",(title,author,year,isbn))
	conn.commit()
	curs.close()
	conn.close()

def searchD(dbname,table,isbn):
	print(isbn)
	conn = sqlite3.connect(dbname + ".sqlite")
	curs = conn.cursor()
	curs.execute("select * from " + table + " where isbn = '" + isbn +"'")
	rows = curs.fetchall()
	curs.close()
	conn.close()
	return rows
