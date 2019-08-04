
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
