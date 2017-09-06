n= int(raw_input("Ener Number of inputs: ").strip())
l = []
for i in range(0,n):
    arr = map(int,raw_input("Enter Inputs saperated bys Space : ").strip().split(" "))
    num = (arr[0] * arr[1]) + arr[2]
    l.append(num)
    

for i in l:
    total = 0
    while (i > 0):
        dig = i % 10
        total += dig
        i = i // 10
    print total,
        
