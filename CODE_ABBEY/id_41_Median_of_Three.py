n= int(raw_input("Ener Number of inputs: ").strip())
l = []
for i in range(0,n):
    arr = map(int,raw_input("Enter Numbers Saperated by spaces : ").strip().split(" "))
    for i in arr:
        if i < max(arr) and i > min(arr):
            l.append(i)

    
for i in l:
    
    print i,
