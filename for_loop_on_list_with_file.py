lst = []
i =0
f = open('/home/asm/files.txt','r')
for line in f:
    print (line)
    lst.append(line)
    lst[i] = line[:-1]
    
print (lst)
print (len(set(lst)))
print (len(lst))
