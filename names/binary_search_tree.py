"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # Insert the given value into the tree
    def insert(self, value): # O(log(n)) is dividing each time, with balanced tree
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
                
    # Return True if the tree contains the value
           # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if self.value > target:
            return False if self.left is None else self.left.contains(target)
        
        if self.value < target:
            return False if self.right is None else self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        return self.value if self.right is None else self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.left is not None:
            self.left.for_each(fn)
        
        if self.right is not None:
            self.right.for_each(fn)