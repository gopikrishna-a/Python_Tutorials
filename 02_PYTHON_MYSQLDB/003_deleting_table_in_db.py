import MySQLdb


db = MySQLdb.connect('localhost','root','asm123','TESTDB')
cursor = db.cursor()

#DELETE THE STUDENTS TABLE IN DB IF EXISTS
try:
    cursor.execute("drop table STUDENTS")

except:
    print "STUDENTS table is not presented in DATABASE"

else:
    print "STUDENTS table deleted Successfully from DB"

db.close()
