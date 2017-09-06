n= int(raw_input("Ener Number of inputs: ").strip())
l = []
for i in range(0,n):
    st = raw_input("Enter Ur Sring: ")
    count = 0
    for i in st:
        if i in "aouiey":
            count += 1
    l.append(count)
    
for i in l:
    print i,
