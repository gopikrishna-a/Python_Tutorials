import MySQLdb


db = MySQLdb.connect('localhost','root','password','TESTDB')
cursor = db.cursor()


sql = "INSERT INTO STUDENTS(NAME,AGE,COURSE) VALUES ('%s', '%d', '%s'),('%s', '%d', '%s'),('%s', '%d', '%s');" % ('Gopikrishna', 23, 'ECE','Gopikrishna', 23, 'ECE','Gopikrishna', 23, 'ECE')

cursor.execute(sql)

cursor.execute("select * from STUDENTS;")
data = cursor.fetchall()
print "================================="
print data
db.commit()
db.close()
