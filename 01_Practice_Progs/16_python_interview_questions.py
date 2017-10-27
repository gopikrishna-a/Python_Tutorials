import subprocess

data = subprocess.check_output('ls')
print(data)

file = open('new_file.txt','w')
file.write(data)
file.close()



a = [[1,2,3],[4,5,6]]

mn = []
mx = []

for i in a:
    mn.append(min(i))
    mx.append(max(i)) 

print(min(mn))
print(max(mx))
