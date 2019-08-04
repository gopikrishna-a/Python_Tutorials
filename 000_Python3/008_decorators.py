
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


#Pass parameters to a decorator function

def outer(name):
    def upper_dec(func):
        """Decorator one two change the case to lower to upper"""
        def inner():
            res = func()
            return res.upper() + name.upper()
        return inner
    return upper_dec

@outer(" gopikrishna")
def say():
    return "good morning"

print(say())



#General decorator for multiple functions


def general_dec(func):
    def inner(*args):
        is_zero = args[1:]
        for i in is_zero:
            if i == 0:
                return "Please provice non- zero denominator"
        return func(*args)
    return inner
@general_dec
def div_one(a, b):
    return a/b

@general_dec
def dive_two(a, b, c):
    return a/b/c

print(div_one(1, 0))
print(dive_two(1, 3, 6))


#Method Decorator
def method_dec(method):
    def inner(name_ref):
        if name_ref.name == "gopikrishna":
            print("Hello!! ", name_ref.name)
        else:
            method(name_ref)
    return inner
    
class Printing(object):
    def __init__(self, name):
        self.name = name
    @method_dec
    def print_name(self):
        print("Your name is: ", self.name)

a = Printing("gopikrishna")
a.print_name()


#Class Decorator

class Decorator:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        str1 = self.func()
        return str1.upper()

@Decorator
def greet():
    return "good morniing"

print(greet())
