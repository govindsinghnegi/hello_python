import numpy as np

# List comprehension would nest in the same way for loops and if statements nest.
# List comprehension loads the entire output list into memory.
# when working with large lists (e.g. 1 billion elements), list comprehension should be avoided. Use generators instead.

# flatten a list of lists using a nested list comprehension
print("flattening a list containing another list")
non_flat = [[1, 2, 3], [4, 5, 6], [7, 8]]
#flat_list = [inner_item for inner_item in outer_item for outer_item in non_flat]   # wrong order
flat_list = [inner_item for outer_item in non_flat for inner_item in outer_item]
print(flat_list)
# include only lists with more than 2 elements in the flattening (so [7,8] should not be included)
print("processing list with 2 elements")
flat_list_more_than_2 = [inner_item for outer_item in non_flat if len(outer_item) > 2 for inner_item in outer_item]
print(flat_list_more_than_2)
# Vs.
flat_list_more_than_2 = [inner_item for outer_item in non_flat for inner_item in outer_item if len(outer_item) > 2]
print(flat_list_more_than_2)
# get a list of all the letters of these words along with the index of the list they belong to but only for words with
# more than two characters
print("processing sub-string with indices")
strings = [['foo', 'bar'], ['baz', 'taz'], ['w', 'koko']]
string_flat = [(inner_item, index) for index, item in enumerate(strings) for outer_item in item if len(outer_item) > 2
               for inner_item in outer_item]
print(string_flat)
# iterate through 2D array
print("processing numpy array")
arr = np.random.randint(10, size=(4, 4))
print(arr)
max_per_row = [max(outer_item) for outer_item in arr]
print(f"max per rows: {max_per_row}")


if __name__=='__main__':
    print("hello list comprehension")