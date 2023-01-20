import time

# callback via classes

def evaluate_with_num(callback = None):
    res = 0
    for i in range(5):
        res += i * i
        time.sleep(1)
        if callback:
            callback(i)
    return res

class Message:
    def __init__(self, content):
        self.content = content
    def __call__(self, num):
        print(f"{num} {self.content}")

print("num + message using class")
message = Message("evaluation is done")
print(evaluate_with_num(message))

#### using before & after processing ####
def evaluate_with_num(callback = None):
    res = 0
    for i in range(5):
        if callback and hasattr(callback, "before_call"):   # using if callback.before_call() will directly invoke it
            callback.before_call(i)
        res += i * i
        time.sleep(1)
        if callback and hasattr(callback, "after_call"):    # # using if callback.after_call() will directly invoke it
            callback.after_call(res)
    return res

class MessageWithBeforeAndAfter:
    def __init__(self):
        pass
    def before_call(self, num, *args):
        print(f"before iteration {num}")
    def after_call(self, res, *args):
        print(f"after iteration res: {res}")

print("enabling before and after processing")
message_before_after = MessageWithBeforeAndAfter()
print(evaluate_with_num(message_before_after))

if __name__=="__main__":
    print("callback via classes")