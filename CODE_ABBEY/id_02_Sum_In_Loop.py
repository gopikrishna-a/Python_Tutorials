n= int(raw_input("Enter No. of Test cases: ").strip())
l = []

for i in range(0,n):
    arr = map(int,raw_input("Enter values saperated by space:").strip().split(" "))
    res = sum(arr)
    l.append(res)
for i in l:
    print i,
