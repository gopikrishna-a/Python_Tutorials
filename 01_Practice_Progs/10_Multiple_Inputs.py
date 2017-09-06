#Taking Size of the list
n = int(raw_input().strip())

#Adding inputs into arr list saperated by ","
arr = map(int,raw_input().strip().split(','))

print arr






n = int(raw_input("Plase enter number of inputs :").strip())
arr = map(int,raw_input("Enter ur input numbers saperated by white space : ").strip().split(' '))
while len(arr) != n:
    arr = map(int,raw_input("Oops no. of inputs not matched Enter again: ").strip().split(' '))
print arr
