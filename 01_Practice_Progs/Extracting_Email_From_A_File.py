import re
file = open("out.txt","r")
string = file.read()
match = re.findall(r'[\w\.-]+@[\w\.-]+', string)
lst = []
for i in match:
    print i
    
