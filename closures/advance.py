


# every function in Python has a special attribute called __closure__, which stores all the “remembered” values
print("__closure__ demo")
def outer_func():
    name = "Thor"
    def print_name():
        print(name)
    return print_name

f = outer_func()
print(f"outer_func.__closure__: {outer_func.__closure__}")
print(f"f.__closure__: {f.__closure__}")
print(f"f.__closure__[0].cell_contents: {f.__closure__[0].cell_contents}")

# closures with bug
print("closure with bug")
def funct_generator():
    funcs = []
    for i in range(3):
        def f():
            return i * 2
        funcs.append(f)
    return funcs

f1, f2, f3 = funct_generator()
print(f"f1(): {f1()}")
print(f"f2(): {f2()}")
print(f"f3(): {f3()}")
print(f"f1.__closure__[0].cell_contents: {f1.__closure__[0].cell_contents}")
print(f"f2.__closure__[0].cell_contents: {f2.__closure__[0].cell_contents}")
print(f"f3.__closure__[0].cell_contents: {f3.__closure__[0].cell_contents}")

# fixing the closure bug
print("after fixing the bug")
def funct_generator2():
    funcs = []
    for i in range(3):
        def f(j=i):
            return j * 2    # f is no more a closure
        funcs.append(f)
    return funcs

f12, f22, f32 = funct_generator2()
print(f"f12(): {f12()}")
print(f"f22(): {f22()}")
print(f"f32(): {f32()}")

# decorators in Python are just extensive applications of closures.
# use lambda function to simplify the code
def outer_func_with_lambda():
    name = "Thor"
    return lambda _: print(name)    # closure helps in protecting private members effectively

f = outer_func_with_lambda()
print(f"f.__closure__: {f.__closure__}")
print(f"f.__closure__[0].cell_contents: {f.__closure__[0].cell_contents}")



if __name__=="__main__":
    print("advance closure")