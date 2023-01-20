

# enclosing function vs. nested function
# Closure is an inner function object, that remembers and has access to variables in the local scope in which it was
# created even after the outer function has finished executing.
# It can also be defined as a means of binding data to a function without passing it as a parameter.
# Even if values in enclosing scopes are not present in memory, closure is a function object that remembers those values.
# Objects can be described as data with methods attached, while closures are functions with data attached.
# Characteristics of a python closure function :
#   1. It is a nested function
#   2. The closure will have access to a 'free' variable that is in outer scope
#   3. It will be returned from the enclosing (outer) function
#   4. It is capable of remembering values present in outer functions (enclosing scopes)
# Adv of closure is data hiding as you never call the inner function directly

def divider(y):
    def divide(x):
        return x / y
    return divide
# divide() is a closure
d1 = divider(2)
d2 = divider(5)
d3 = divider(4)
# d1, d2 & d3 are instances of a closure
print(d1(20))
print(d2(20))
print(d3(20))


# deletion of enclosing function
def outer_func():
    name = "Thor"
    def print_name():
        print(name)
    return print_name

f = outer_func()
print(f"type(f): {type(f)}")
del outer_func
f()
print(f"type(f) after deletion: {type(f)}")
# outer_func()  #NameError: name 'outer_func' is not defined

# executing closure before returning
def outer_func():
    name = "Thor"
    def print_name():
        print(name)
    return print_name()     # inner function is already executed before returning

f = outer_func()
print(f"type(f): {type(f)}")
# f()       #'NoneType' object is not callable






if __name__=="__main__":
    print("hello closure")

