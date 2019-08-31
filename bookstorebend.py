import psycopg2
 connection = psycopg2.connect(user = "postgres",
                                  password = ".......",
                                  host = "127.0.0.1",
                                  port = "8080",
                                  database = "myfirst")
def connect():
	
	 cur = connection.cursor()
	 cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title CHARACTER VARYING , author CHARACTER VARYING , year INTEGER , isbn INTEGER)")
	 connection.commit()
	 connection.close()


def insert(title,author,year,isbn):
	
	cur = connection.cursor()
	cur.execute("INSERT INTO book(title,author,year,isbn)VALUES('%s','%s',%d,%d)"%(title,author,year,isbn))
	connection.commit()
	connection.close()


def view():
	
	cur = connection.cursor()
	cur.execute("Select * from book")
	rows=cur.fetchall()
	connection.close()
	return rows

def search(title="",author=""):
	
	cur = connection.cursor()
	cur.execute("Select * from book where title='%s' OR author='%s' "%(title,author))
	rows=cur.fetchall()
	connection.close()
	return rows

def delete(id):

	cur = connection.cursor()
	cur.execute("delete from book where id = %d"%(id))
	connection.commit()
	connection.close()

def update(id,title,author,year,isbn):
	
	cur = connection.cursor()
	cur.execute("UPDATE book SET title='%s' , author='%s' , year=%d , isbn=%d where id='%d'"%(title,author,year,isbn,id)) 
	connection.commit()
	connection.close()





connect()

