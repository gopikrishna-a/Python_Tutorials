import MySQLdb


db = MySQLdb.connect('localhost','root','password','TESTDB')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print data
db.close()
