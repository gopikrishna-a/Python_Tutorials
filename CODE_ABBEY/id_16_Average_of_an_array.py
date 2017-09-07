
#Method --> 1

N= int(raw_input("Enter No. of Test cases: ").strip())
l = []

for i in range(0,N):
    arr = map(float,raw_input("Enter values saperated by space:").strip().split(" "))
    total = 0
    cnt = 0
    for i in arr:
        if i != 0:
            total += i
            cnt += 1
    avg = int(round(total / cnt))
    l.append(avg)

for i in l:
    print i,
    
    
#Method --> 2

N= int(raw_input("Enter No. of Test cases: ").strip())
l = []

for i in range(0,N):
    arr = map(float,raw_input("Enter values saperated by space:").strip().split(" "))
    arr = arr[:-1]
    avg = int(round(sum(arr) / len(arr)))
    l.append(avg)

for i in l:
    print i,
    
