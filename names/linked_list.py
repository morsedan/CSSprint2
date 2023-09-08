class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None # Stores a node that corresponds to our first node in the list
        self.tail = None # Stores a node that is the end of the list
    
    def add_to_head(self, value):
        # Create a node to add
        new_node = Node(value)
        # Check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # Move head to new node
            self.head = new_node
    
    def add_to_tail(self, value):
        # Create a node to add
        new_node = Node(value)
        # Check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            # Point the node at the current tail to the new node
            self.tail.next_node = new_node

        self.tail = new_node
    
    def remove_head(self):
        # If list is empty, do nothing
        if not self.head:
            return None
        # If list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None 
            return head_value
        # More items in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
    
    def contains(self, value):
        if self.head is None:
            return False
        
        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head
        
        while current_node is not None:
            # Check if this is the node we are looking for
            if current_node.value == value:
                return True
            
            # Otherwise, go to the next node
            current_node = current_node.next_node
        return False
    
    def count(self):
        current = self.head
        i = 0
 
        while current:
            current = current.next_node
            i += 1
        
        return i