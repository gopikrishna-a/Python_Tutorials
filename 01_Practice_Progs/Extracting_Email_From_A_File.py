import re
file = open("out.txt","r")
string = file.read()
match = re.findall(r'[\w\.-]+@[\w\.-]+', string)
for i in match:
    print i
    
