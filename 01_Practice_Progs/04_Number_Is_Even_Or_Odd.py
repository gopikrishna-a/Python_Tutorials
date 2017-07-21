def Odd_Or_Even(n):
    if n % 2 ==0:
       print "Number",n,"is Even\n"
    else:
       print "Number",n,"is Odd\n"

while True:
    a = raw_input("Enter Ur Number:")
    try:
        a = int(a)
        Odd_Or_Even(a)
    except ValueError:
        print "Enter Only Numbers\n"
