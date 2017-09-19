import MySQLdb


db = MySQLdb.connect('localhost','root','password','TESTDB')
cursor = db.cursor()

#Try to create the STUDENTS table if not daabase
try:
    sql = """CREATE TABLE STUDENTS (
             NAME CHAR(20),
             AGE INT,
             COURSE CHAR(20));"""
    cursor.execute(sql)

except:
    print "Table STUDENTS already created"
    
else:
    print "Table created Successfully"

db.close()
