"""
triangle inequality theorem

A + B > C
B + C > A
C + A > B

A,B,C are sides of a triangle
"""



n = int(raw_input("Enter No. of Inputs : ").strip())
l = []
for i in range(0,n):
    arr = map(float,raw_input("Enter The sides of the triangle saperated by space : ").strip().split(" "))
    tr = 0
    if ((arr[0] + arr[1]) > arr[2]) and ((arr[1] + arr[2]) > arr[0]) and ((arr[0] + arr[2]) > arr[1]):
        tr = 1
    else:
        tr = 0
    l.append(tr)

for i in l:
    print i,
