from collections.abc import Sequence

class FixedSizeArray(Sequence):
    "Implements a fixed sized array sequence"

    def __init__(self):
        self.A = []
        self.size = 0

    def build(self, X):
        "Simulate fix sized array with Python list"
        self.A = [a for a in X]
        self.size = len(X)

    def get_at(self, i):
        "Return value stored at index i"
        if i < 0 or i >= self.size:
            raise IndexError('Index out of bounds')
        if not isinstance(i, int):
            raise KeyError('Only accepting integers for index')
        return self.A[i]
    
    def set_at(self, i, val):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of bounds')
        if not isinstance(i, int):
            raise KeyError('Only accepting integers for index')
        self.A[i] = val

    def __len__(self):
        return len(self.A)
    
    def __getitem__(self, key: int):
        if key < 0 or key >= self.__len__():
            raise IndexError('Index out of bounds')
        return self.A[key]

    def __str__(self):
        return str(self.A)

a = FixedSizeArray()

a.build(range(0, 15, 2))
print(a)
