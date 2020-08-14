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
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        current = self
        while current is not None:
            if target < current.value:
                if current.left is None:
                    return False
                else:
                    current = current.left
            elif target > current.value:
                if current.right is None:
                    return False
                else: 
                    current = current.right
            else:
                return True 



bst = BSTNode(names_1[0])
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


# all_names = None
# for name in names_1:
#     if all_names is None:
#         all_names = BSTNode(name)
#     else:
#         all_names.insert(name)

# for name in names_2:
#     if all_names.contains(name):
#         duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
