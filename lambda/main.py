# lambda <argument(s)> : <expression>
# lambdas are one-liner functions
# lambda is an IIFE-Immediately Invoked Function Expression
# lambda <expr>: <expr> if <cond> else <expr>
# You cannot have multiple statements in a lambda expression
# Higher Order Function->map, filter & reduce
# lambda can be used with the key parameter, e.g sorted(list, key=lambda)
# A lambda function inside a lambda function is called a nested lambda function

import functools

# find min of 3 variables
my_min = (lambda a, b, c: a if (a <= b) and (a <= c) else (b if (b <= c) else c))(4, 12, 3)

# convert each element of tuple = ( 2.88, -1.75, 100.55 ) into int
my_tuple = tuple(map(lambda x: int(x), (2.88, -1.75, 100.55)))

# For a given list [28, -15, 7, 13, 11], numbers from the range [10; 20] are formed
my_list = list(filter(lambda x: (x >= 10 and x <= 20), [28, -15, 7, 13, 11]))

# For [2, 3, 9] calculate the sum of the elements of a sequence
my_sum = functools.reduce(lambda x, y: x + y, [2, 3, 9])

if __name__ == '__main__':
    print('hello lambda')
    print(my_min)
    print(*my_tuple)
    print(*my_list)
    print(my_sum)

