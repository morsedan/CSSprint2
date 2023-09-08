# sourcery skip: ensure-file-closed, for-append-to-extend, list-comprehension, move-assign-in-block
from binary_search_tree import BSTNode
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
"""
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""

rootNode = BSTNode(names_1[0])

for name in names_1[1:]:
    rootNode.insert(name)

for name in names_2:
    if rootNode.contains(name):
        duplicates.append(name)

end_time = time.time()
print("--------------------------------------------\nBST")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_times = time.time()

f = open('names_1.txt', 'r')
names_1s = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2s = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

names_set_1 = set(names_1s)
names_set_2 = set(names_2s)

# Find duplicates using sets
duplicates = list(names_set_1 & names_set_2)

end_times = time.time()
print("--------------------------------------------\nSets")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_times - start_times} seconds")

print(f"--------------------------------------------\nSets ran {(end_time - start_time) / (end_times - start_times)} times faster")