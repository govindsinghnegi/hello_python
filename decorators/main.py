
# decorator is a function that takes another function as its argument, and returns yet another function.
# they allow the extension of an existing function, without any modification to the original function source code.

def simple_add(a, b):
    return a+ b

print(f"simle 2+3 = {simple_add(2, 3)}")

## extend functionality of simple_add to accept a list of 2-element tuple and return a list of summation of indiv item.
def tuple_addition(func):
    def add_tuple(list_of_tuples):
        return [func(a, b) for (a, b) in list_of_tuples]
    return add_tuple
@tuple_addition  # is equivalent to simple_add_together = tuple_addition(simple_add_together)
def simple_add_with_decorator(a, b):    # because of decorator this function now points to inner function of decorator
    return a + b

print(f"[(1, 2), (2, 3), (3, 4)] using decorator = {simple_add_with_decorator([(1, 2), (2, 3), (3, 4)])}")

#### decorator with arguments ####
# extend the above logic to power the summation with an int argument given to the tuple_addition decorator.
# to add an argument to a decorator, define a new decorator
def add_power(power):
    def tuple_addition(func):
        def add_tuple(list_of_tuples):
            return [func(a, b) ** power for (a, b) in list_of_tuples]
        return add_tuple
    return tuple_addition

@add_power(2)
def simple_add_with_power_decorator(a, b):
    return a+b

print(f"[(1, 2), (2, 3), (3, 4)] using argument decorator = {simple_add_with_power_decorator([(1, 2), (2, 3), (3, 4)])}")


#### default argument in decorators ####

def add_power_with_default(arg):
    def tuple_addition(func):
        def add_tuple(list_of_tuples):
            return [func(a, b) ** power for (a, b) in list_of_tuples]
        return add_tuple
    if callable(arg):
        power = 2
        return tuple_addition(arg)
    else:
        power = arg
    return tuple_addition

@add_power_with_default(3)
def simple_add_with_power_decorator(a, b):
    return a+b

print(f"[(1, 2), (2, 3), (3, 4)] using argument decorator = {simple_add_with_power_decorator([(1, 2), (2, 3), (3, 4)])}")

print("using default val for decorator")

@add_power_with_default
def helloo(a, b):
    return a+b

print(f"[(1, 2), (2, 3), (3, 4)] using default argument decorator = {helloo([(1, 2), (2, 3), (3, 4)])}")




if __name__ == "__main__":
    print("hello decorators")
