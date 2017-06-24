magicNumber = 26

# This program finds a magic number
for number in range(101):
    if number is magicNumber:
        print "The magic number is:",magicNumber
        break
    else:
        print number,"Is not a magic Number"
