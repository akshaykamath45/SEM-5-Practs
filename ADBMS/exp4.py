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
