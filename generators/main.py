
# generator is a function that behaves like an iterator by returning a (lazy) iterator object which we can then iterate over.
# the code in generator functions only execute when next() is called on the generator object.
# Local variables and their states are remembered between successive calls.
# Methods like __iter__() and __next__() are implemented automatically in generator.
# If a function contains at least one yield statement it becomes a generator function.
# Once the function yields, the function is paused and the control is transferred to the caller.
# vs. return: return statement terminates a function entirely but a yield statement pauses the function saving all its
# states and later continues from there on successive calls.
# Finally, when the function terminates, StopIteration is raised automatically on further calls.
# generator object can be iterated only once.
# As lambda functions create anonymous functions, generator expressions create anonymous generator functions.
# a list comprehension produces the entire list while the generator expression produces one item at a time.Thus,
#  a generator expression is much more memory efficient than an equivalent list comprehension.
# Generators are slower than Iterators, so trade-off between memory vs. speed
# Generators are excellent mediums to represent an infinite stream of data.
# advanced generator methods: .send(), .throw(), .close()


#### get only odds via custom iterator
class OddNumbers:
    def __init__(self, max):
        self.start = -1
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        self.start += 2
        if self.start > self.max:
            raise StopIteration
        else:
            return self.start

print("odd numbers via custom iterator")
for count in OddNumbers(5):
    print(count)

#### get odd via generators

def odd_numbers(max):
    start = 1
    while start <= max:
        yield start
        start += 2

print("odd numbers via simple generator")
for count in odd_numbers(5):
    print(count)

#### infite sequence generator
def infite_sequence():
    start = 0
    while True:
        yield start
        start += 1

#### reading large files
def csv_reader():
    file = open("some_file.csv")    # open() creates a generator
    result = file.read().split("\n")   # but read().split() loads everything into memory
    return result

def csv_reader_new():
    file = open("some_file.csv")
    for row in file:
        yield row

def csv_reader_using_expr():
    csv_gen = (row for row in open("some_file.csv"))
    return csv_gen

print("list comprehension")
print([num**2 for num in range(5)])
print("generator comprehension")
print((num**2 for num in range(5)))


if __name__ == "__main__":
    print("hello generators")
