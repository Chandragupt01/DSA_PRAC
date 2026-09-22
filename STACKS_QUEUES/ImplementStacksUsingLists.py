class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.n=n
        self.items=[]

    
    def isEmpty(self):
        # Check if stack is empty
        if len(self.items)==0:
            return True
        return False

    
    def isFull(self):
        # Check if stack is full
        if len(self.items)==self.n:
            return True
        return False
        

    
    def push(self, x):
        # Insert x at the top of the stack
        self.items.append(x)

    
    def pop(self):
        # Removes an element from the top of the stack
        if len(self.items)==0:
            return -1
        return self.items.pop()

    
    def peek(self):
        # Returns the top element of the stack
        if len(self.items)==0:
            return -1
        return self.items[-1]
        