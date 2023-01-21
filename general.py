import copy
from typing import List, Dict, Union, Optional


####### *args **kwargs  ######
# print() & os.join() built-in functions
# *args: packs the received arguments in a tuple named args
# * operator: comes before an iterable and spread out its element as the arguments of the function
# function(*[1,2,3]) = function(1,2,3)
# when using *args with positional arguments, it must come in the last. But default value arguments can still come in the last

def multiply_numbers(*numbers):
    print(type(numbers))
    product = 1
    for num in numbers:
        product *= num
    return product


##### **kwargs  ######
# When using **kwargs, all the keywords arguments you pass to the function are packed inside a dictionary
# order when positional arg + default value arg + *args + **kwargs: pos_args>*args>def_val_args>**kwargs

def show_user_info(**data):
    print(type(data))
    for key, value in data.items():
        print(f"{key}: {value}")


def order_of_args(a, b, *args, c=10, **kwargs):
    print(f"positional args: {a} & {b}")
    print(f"*args: {args}")
    print(f"default args: {c}")
    print(f"**kwargs: {kwargs}")


##### Union on a Variable #####
def print_union():
    mylist: List[Union[int, str]] = ["a", 1, "b", 2]
    print(type(mylist))
    print(mylist)


##### Optional #####
# Optional[type] is shorthand or alias for Union[type, None]
# Whenever you have a keyword argument with default value None, you should use Optional as it helps in type hinting
# Optional[Union[str, int]] and Union[str, int, None] are exactly the same thing
# Python 3.10 introduces the | union operator, so instead of Union[str, int] you can write str | int

def without_optional(a: dict = None):
    if a:
        print(a)
    else:
        print("empty dict")


def with_options(a: Optional[Dict] = None):
    if a:
        print(a)
    else:
        print("empty dict")


##### copy ######
# assignment vs. copy vs. deep copy
# Assignment statements in Python do not create copies of objects, they only bind names to an object.
# shallow copy: create a new object then add all the references as its contents, it is only one-level deep.
# Therefore, the copy is not fully independent of the original.
# deep copy: create a new object then recursively add the contents. The clone is fully independent of the original,
# but creating a deep copy is slower.
# You can copy arbitrary objects (including custom classes) with the copy module.
# For immutable objects, since they don't change, python does not create a new object and just create a new reference.
# For mutable objects, since they can change, python creates a new object and (shallow) copy the content of main object.

print("Copying in python")
# Python built-in mutable collections (lists, dicts, and sets) can be shallow-copied by calling their factory functions
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
print(f"xs: {xs} vs. ys: {ys}")
print(xs is ys)
print(xs[0] is ys[0])
xs.append(['new sublist'])
print("after appending to xs")
print(f"xs: {xs} vs. ys: {ys}")
xs[1][0] = 'X'
print("after changing value of a reference")
print(f"xs: {xs} vs. ys: {ys}")
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)  # copy.copy(xs) will create a shallow copy
print(f"xs: {xs} vs. zs: {zs}")
xs[1][0] = 'X'
print("after changing value of a reference")
print(f"xs: {xs} vs. zs: {zs}")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')

rect = Rectangle(Point(0, 1), Point(5, 6))
s_rect = copy.copy(rect)
print(f"rect: {rect} vs. s_rect: {s_rect}")
rect.topleft.x = 999
print("after changing x")
print(f"rect: {rect} vs. s_rect: {s_rect}")
d_rect = copy.deepcopy(s_rect)
d_rect.topleft.x = 222
print("after changing x")
print(f"rect: {rect} vs. s_rect: {d_rect}")

#### 5 usage scenarios of asterisks ####
# scenario 1, multiplication
print(f"2*3: {2*3}")
print(f"2**3: {2**3}")

# scenario 2, Receive an Unlimited Number of Arguments
def print_multiple_args(*args, **kwargs):
    print("print_multiple_args: hello world")
print_multiple_args()

# scenario 3, Restrict to Keyword-Only Arguments
def keyword_args_only(*, first, second):
    print(f"keyword_args_only: first: {first} and second: {second}")
keyword_args_only(first='hello', second='world')

# scenario 4,  Iterables Unpacking
A = [1, 2, 3]
B = ("a", "b", "c")
C = {7.1, 8.2, 9.3}
L = [a for a in A] + [b for b in B] + [c for c in C]
print(f"L = {L}")
L = [*A, *B, *C]
print(f"L = {L}")
D = {'first': 1, 'second': 2, 'third': 3}
print(*D)
# first second third
# print(**D)
# TypeError: 'first' is an invalid keyword argument for print()
# because we must use their keys to receive the unpacked values.
print('{first},{second},{third}'.format(**D))

# scenario 5 Extended Iterable Unpacking
# This unpacking syntax was introduced by PEP 3132 to make our code more elegant.
# This PEP proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name which will be
# assigned a list of all items not assigned to a “regular” name.
L = [1, 2, 3, 4, 5, 6, 7, 8]
a, *b = L
print(f"a = {a}")
print(f"b = {b}")



if __name__ == '__main__':
    print("hello-general")
    # *args
    print(multiply_numbers())
    print(multiply_numbers(5, 2))
    print(multiply_numbers(2, 3, 4, 5))
    print(multiply_numbers(2, 3, [1, 2]))
    # **kwargs
    show_user_info(name="govind")
    show_user_info(name="govind", gender="Male")
    # all args
    order_of_args(1, 2, 3, 4, d=-5, e=-7)
    # union
    print_union()
    # optional
    without_optional()
    without_optional({"one": 1, "two": 2})
    with_options()
    with_options({"three": 3, "four": 4})
