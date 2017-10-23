#Triangle pattern
"""
input: 5

Output:

#####
####
###
##
#

"""

#code for pattern: 1
def print_triangle(num):
    cnt = num
    for i in range(num):
        print('#' * cnt)
        cnt -= 1
    return " Pattern printed"
    
    
    
num = int(input('Enter ur input number: '))
print(print_triangle(num))



#code for pattern: 2
"""
input: 5
out put:
    
#
##
###
####
#####

"""

def print_triangle(num):
    cnt = 1
    for i in range(num,0,-1):
        print('#' * cnt)
        cnt += 1
    return " Pattern printed"
    
    
    
num = int(input('Enter ur input number: '))
print(print_triangle(num))

