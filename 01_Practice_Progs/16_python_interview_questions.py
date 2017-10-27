
###################################################################################
import subprocess

data = subprocess.check_output('ls')
print(data)

file = open('new_file.txt','w')
file.write(data)
file.close()

###################################################################################

a = [[1,2,3],[4,5,6]]

mn = []
mx = []

for i in a:
    mn.append(min(i))
    mx.append(max(i)) 

print(min(mn))
print(max(mx))

###################################################################################

#Method--> 1
l = []
for i in range(15,50):
    if i % 5 == 0:
        l.append(i)
print(l)

#Method--> 2
l = [i for i in range(15,50) if i % 5 == 0]
print(l)



###################################################################################



import re

txt = "Gopikrishna ankdjm sjd Asm "
obj = re.compile(r'[A-Z]+[a-z]+')
print(re.findall(obj,txt))
