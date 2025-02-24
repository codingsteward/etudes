# Stack 

class ArrayStack:

    def __init__(self, capacity=10):
        '''Top points to the index where last element is inserted, -1 if empty'''
        self.data = [None]*capacity
        self.capacity = capacity
        self.top = -1

    def push(self, item):
        if self.top == self.capacity-1:
            raise IndexError('exceeds capacity')
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if self.empty():
            raise IndexError('pop from empty list')
        self.top -= 1
        return self.data[self.top+1]
    
    def empty(self):
        '''Stack is empty is top is 0'''
        return self.top == -1
