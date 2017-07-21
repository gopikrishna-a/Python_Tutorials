#Method One
a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,88,77])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,55,66,77,88])
lst = []
for i in a:
    for k in b:
        if i == k:
            lst.append(i)
print lst

#Method Two

a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,88,77])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,55,66,77,88])
print (a & b)
