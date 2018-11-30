#program to compare three numbers!!

def compare_three_nums(a,b,c):


	if a > b and a > c:
	    return ("a is bigger!!")
	    
	elif b > a and b > c:
	    return ("b is bigger!!")
	    
	elif c > a and c > b:
	    return ("c is bigger!!")
	    
	elif a == b == c:
	    return ("all are equal!!")
	    
	elif a == b and a > c:
	    return ("a and b are equal and bigger than c!!")
	    
	elif a == c and a > b:
	    return ("a and c are equal and bigger than b!!")
	    
	elif b == c and b > a:
	    return ("b and c are equal and bigger than a!!")
	    
	else:
	    return ("Oops something went wrong!!")


a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))

print(compare_three_nums(a,b,c))
