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


def print_triangle(num):
    cnt = num
    for i in range(num):
        print('#' * cnt)
        cnt -= 1
    return " Pattern printed"
    
    
    
num = int(input('Enter ur input number: '))
print(print_triangle(num))

