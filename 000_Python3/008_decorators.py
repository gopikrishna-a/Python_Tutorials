
#Decorator without any arguments

def decorator_func(func):
    def add_change():
         res = func()
         return res.capitalize()
    return add_change

@decorator_func
def say():
    return "good morning"

print(say())


#Decorator with any arguments
def div_dec(func):
    def handle_error(a, b):
        try:
            res = func(a, b)
            return res
        except ZeroDivisionError:
            return "Try Again with non zero denominator"
    return handle_error
@div_dec 
def div(a, b):
    return a/b

print(div(2, 3))


#Multiple Decorator

def upper_dec(func):
    """Decorator one two change the case to lower to upper"""
    def add_change():
        res = func()
        return res.upper()
    return add_change

def split_dec(func):
    """Decorator function two to split the string"""
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper

@split_dec
@upper_dec
def say():
    return "good morning"

print(say())
