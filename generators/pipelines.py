import math


#### generator pipeline
# case1:
# for each number from a range of integers, you want to apply the following calculations:
#   1. square the number
#   2. add the square root of pi
#   3. take the square root
#   4. return the result after rounding to two decimal digits

def power(x, power):
    return x ** power

def add(x, y):
    return x + y

def without_pipeline(num):
    return (
        (
        round(power(add(power(n, 2), power(math.pi**.5)), 0.5), 2)
    )
    for n in range(num)
    )

def with_pipeline(num):
    step_1 = (power(n, 2) for n in range(num))
    step_2 = (add(power(n, 2), power(math.pi**.5)) for n in step_1)
    step_3 = (power(add(power(n, 2), power(math.pi**.5)), 0.5) for n in step_2)
    step_4 = (round(power(add(power(n, 2), power(math.pi**.5)), 0.5), 2) for n in step_3)
    return step_4

def calculate(n):
    n = power(n, 2)
    n = add(n, power(math.pi**.5))
    n = power(n, 0.5)
    n = round(n)
    return n

def with_better_pipeline(num):
    return (calculate(n) for n in range(num))

#### general pipeline
"""
general pipeline structure shall follow:
def operations(x_i):
    step1 = function1(x_i)
    step2 = function2(step1)
    step3 = function3(step2)
    return function4(step3)

results = (operations(x_i) for x_i in x)
# or
results = map(operations, x)
"""



if __name__=="__main__":
    print("hello generators pipeline")