
N= int(raw_input("Enter No. of Test cases: ").strip())
l = []

arr = map(str,raw_input("Enter values saperated by space:").strip().split(" "))
if len(arr) == N:
    for i in arr:
        res = 0
        cnt = 1
        i = int(i[::-1])
        while i > 0:
            dig = i % 10
            res += (dig * cnt)
            i = i / 10
            cnt += 1
        l.append(res)
else:
    print "Oops! No. of test cases and No. of values mismatched "
    
for i in l:
    print i,
    
    
