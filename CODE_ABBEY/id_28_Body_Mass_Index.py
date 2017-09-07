n = int(raw_input("Enter No. of Inputs : ").strip())
l = []
for i in range(0,n):
    arr = map(float,raw_input("Enter The weight and Height saperated by space : ").strip().split(" "))
    BMI =  arr[0] / (arr[1] ** 2 )
    l.append(BMI)

for i in l:
    if i < 18.5:
        print "under",
    elif i >= 18.5 and i < 25.0:
        print "normal",
    elif i >= 25.0 and i < 30.0:
        print "over",
    elif i >= 30.0:
        print "obese",
