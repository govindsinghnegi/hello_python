#### iterables vs. iterators
# iterable object implements the __iter__() method and returns an iterator object, examples are list, set and string
# iterator object implements the __next__() method in a way that:
#   * the next value of an iterable object is being returned and the state of the iterator gets updated so that it points to the next value
#   * raises a StopIteration when the elements of the iterable object are exhausted
# additionally, an Iterator is an Iterable itself as it must also implement __iter__() method where it simply returns self.
# every iterator is an iterable too but not every iterable is an iterator

print("iterable vs. iterator")
my_lst = [5, 10, 15]
my_iter = iter(my_lst)
print(f"type of my_iter: {my_iter}")
print(f"my_iter.__next__(): {my_iter.__next__()}")  # my_iter.__next__() = next(my_iter)

print("building a custom iterator")
class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration

for c in Counter(3, 7):
    print(c)

if __name__ == "__main__":
    print("hello iterators")