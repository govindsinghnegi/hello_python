import time

print("without callback")
def evaluate(callback = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if callback:
            callback()
    return res

print(f"final res: {evaluate()}")

print("with callback")
def print_callback():
    print("Evaluation done!")

print(f"final res: {evaluate(print_callback)}")

print("with callback with params")
def evaluate_with_num(callback = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if callback:
            callback(i)
    return res
def print_with_param_callback(num):
    print(f"{num} evaluation done!")

print(f"final param res: {evaluate_with_num(print_with_param_callback)}")

if __name__ == "__main__":
    print("hello callables")