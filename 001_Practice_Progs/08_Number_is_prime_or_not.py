def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            print "Not a Prime"
            break
    else:
        print "Number is a Prime"
while True:
    num = int(raw_input("Enter Ur Number : "))
    is_prime(num)
    
    
    
    
    
    
    
    
#Without function
num = 13
for i in range(2,num):
    if num % i ==0:
        print "Not a Prime"
        break
else:
    print "Prime"
