"""
Arithmetic progression

Definition:
===========
Arithmetic progression is a sequence, such as the positive odd integers 1, 3, 5, 7, . . . , in which each term after the first is formed by adding a constant to the preceding term.

Formulas:

an = a1 + d(n - 1)

Sn = ((a1 + an) n) / 2

Here:
    a1 = arr[0]
    d = arr[1]
    n = arr[2]
    sn = AP
"""




N= int(raw_input("Enter No. of Test cases: ").strip())
l = []

for i in range(0,N):
    arr = map(int,raw_input("Enter values saperated by space: ").strip().split(" "))
    a1 = arr[0]
    d = arr[1]
    n = arr[2]
    an = a1 + (d * (n -1))
    sn = ((a1 + an) * n) / 2
    l.append(sn)
for i in l:
    print i,
