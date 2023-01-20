import time
from functools import partial

# using closure with callback adds the flexibility of changing the closure without touching the enclosing function

def evaluate_with_num(callback = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if callback:
            callback(i)
    return res

# callback using lambda
print("via lambda")
print(evaluate_with_num(lambda num: print(f"{num} evaluation is done")))

# divide the content into num + message parts and use them via lambda
def print_content(num, message):
    print(f"{num} {message}")

print("num + message via lambda")
print(evaluate_with_num(lambda num: print_content(num, "evaluation is done")))

print("num + message  via partial")
partial_func = partial(print_content, "evaluation is done")
print(evaluate_with_num(partial_func))

# divide the content into num + message parts and use them via function
def print_content_using_closure(message):   # cannot use number in the enclosing function
    def inner_func(num):
        print(f"{num} {message}")
    return inner_func

print("num + message using closure")
print(evaluate_with_num(print_content_using_closure("evaluation is done")))

# change the message string without touching the enclosing method
new_message = "processing is done"
enclosing_func = print_content_using_closure(new_message)
print("num + new message using closure")
print(evaluate_with_num(enclosing_func))



if __name__=="__main__":
    print("advance concepts")