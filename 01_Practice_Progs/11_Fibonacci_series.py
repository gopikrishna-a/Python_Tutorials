# Fibonacci Series Programs

#METHOD -----> 1
# Fibonacci series upto a number(n)

def fib(n):
    a,b = 0,1
    while a<n:
        print (a,end=" ")
        a,b = b,a+b
#input
fib(10)

#output
0 1 1 2 3 5 8 


#METHOD -----> 2
#Fibonacci series of n numbers
#for large number this program will run very slow

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >2:
        return fib(n-1) + fib(n-2)
    
for n in range(0,11):
    print (fib(n))
    

#METHOD -----> 3
#Fibonacci series of n numbers with explicit Memoization
#
fib_cache = {}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >2:
        return fib(n-1) + fib(n-2).
        
    #storing recently calculated fib_series cache
    fib_cache[n] = value
    return value
    
for n in range(0,20):
    print (fib(n))
    
    
    
#METHOD -----> 4
#Fibonacci series of n numbers with implicit Memoization
#this will run faster
#Only works for Python3

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >2:
        return fib(n-1) + fib(n-2)

for n in range(0,20000):
    print (fib(n))
    

    
    
    
#METHOD -----> 5
#Fibonacci series of n numbers 
    
    
b = 0
c = 1
n = 10

for i in range(10):
    if i <= 1:
        temp = i
    else:
        temp = b + c
        b = c
        c = temp
        
    print temp,






















