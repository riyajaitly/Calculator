#
# DO NOT FORGET TO ADD COMMENTS
#
class Stack:
    
    def __init__(self):
        self.elements = []

    #check empty stack
    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    #push an element into stack
    def push(self, item):
        self.elements.append(item)

    #pop an element from the stack
    def pop(self):    
        if self.elements:        
            return self.elements.pop()    
        else:        
            return None

    #retrieve first/top element from stack
    def peek(self):
        t = len(self.elements)
        if t == 0:
            return None
        return self.elements[t-1]

    def size(self):
        return len(self.elements)
