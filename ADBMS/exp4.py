# BTree

from BTrees.IIBTree import IIBTree
import time
t = IIBTree()
insertion_start_time = time.time()
for i in range(1000):
    t.update({i: 2*i})
insertion_end_time = time.time()
print(f"Insertion time: {round((insertion_end_time-insertion_start_time)*1000,3)} milliseconds")
key = int(input("enter key: "))
search_start_time = time.time()
if t.has_key(key):
    print(t[key])
search_end_time = time.time()
print(f"Search time: {round((search_end_time-search_start_time)*1000,3)} milliseconds")


# It imports the IIBTree class from the BTrees.IIBTree module.
# It creates an instance of IIBTree called t.
# It measures the time taken to insert 1000 key-value pairs into the tree, where the keys are integers from 0 to 999, and the values are twice the keys.
# It prompts the user to enter a key and then searches for that key in the tree. If the key is found, it prints the corresponding value.
# It measures the time taken for the search operation.




# BPlusTree

class InMemoryBPlusTree:
    def __init__(self, order):
        self.tree = {}

    def insert(self, key, value):
        self.tree[key] = value

    def search(self, key):
        return self.tree.get(key)

import time

tree = InMemoryBPlusTree(order=50)

for i in range(1000):
    data = (2 * i).to_bytes(10, 'big')
    tree.insert(i, data)

data = int(input("Enter key: "))
start_time = time.time()
byte_data = tree.search(data)
end_time = time.time()

if byte_data:
    int_data = int.from_bytes(byte_data, 'big')
    print("Value:", int_data)
else:
    print(f"No data found for key {data}")

print("Time taken:", (end_time - start_time) * 1000, "ms")


# from bplustree import BPlusTree
# import time
# tree = BPlusTree('D:/b1.db', order=50)
# for i in range(1000):
#     data = (2*i).to_bytes(10, 'big')
#     tree[i] = data
# data = int(input("Enter key : "))
# start_time = time.time()
# byte_data = tree.get(data)
# end_time = time.time()
# int_data = int.from_bytes(byte_data, 'big')
# print("Value : ", int_data)
# print("Time taken : ", (end_time-start_time)*1000, " ms")


# Create B+ Tree and Insert Data:
# A B+ tree is created with a specified order of 50, and 1000 key-value pairs are inserted.
# Each key is an integer from 0 to 999, and the corresponding value is a 10-byte representation of twice the key.

# User Input and Search:
# The user is prompted to enter a key.
# The B+ tree is then searched for the entered key, and the corresponding data in byte form is retrieved.

# Conversion and Output:
# The byte data is converted back to an integer.
# The value associated with the key is printed.
# The time taken for the search operation is also displayed in milliseconds.





