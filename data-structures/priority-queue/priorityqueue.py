# Priority queue implementation
from abc import ABCMeta, abstractmethod

class PriorityQueue(metaclass=ABCMeta):

    @abstractmethod
    def insert(self, item) -> None:
        raise NotImplementedError

    @abstractmethod
    def getMax(self) -> int:
        raise NotImplementedError


class MaxHeap(PriorityQueue):

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.pq = [None]*(self.capacity+1)
        self.size = 0

    def insert(self, item):
        print("inserting %d" % (item))
        self.size += 1
        self.pq[self.size] = item
        self._fixup(self.pq, self.size)

    def getMax(self):
        print("get max")
        if self.size == 0: raise IndexError
        self.pq[1], self.pq[self.size] = self.pq[self.size], self.pq[1]
        self._fixdown(self.pq, 1, self.size-1)
        max_index = self.size
        self.size -= 1
        return self.pq[max_index]

    def _fixup(self, heap, k):
        """Bottom up heapify from node k upwards"""
        while k > 1 and heap[k//2] < heap[k]:
            print("fixing up")
            heap[k//2], heap[k] = heap[k], heap[k//2]
            k //= 2

    def _fixdown(self, heap, k, N):
        """Top down heapify from node k downwards
        If there's 2 children, pick the larger node"""
        while 2*k <= N:
            print("fixing down")
            j = 2*k
            if j < N and heap[j] < heap[j+1]:
                j += 1
            if heap[k] >= heap[j]:
                break
            heap[k], heap[j] = heap[j], heap[k]
            k = j

    def _heapify(self, heap):
        for i in reversed(range(self.size//2)):
            self._fixdown(heap, i, N)

class ArrayBasedPriorityQueue(PriorityQueue):

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.pq = [None]*capacity

    def __len__(self):
        return self.size

    def insert(self, item):
        if self.size == self.capacity:
            raise IndexError
        self.pq[self.size] = item
        self.size += 1

    def getMax(self):
        max_index = 0
        for i in range(1, self.size):
            if self.pq[max_index] < self.pq[i]:
                max_index = i
        self.pq[max_index], self.pq[self.size-1] = self.pq[self.size-1], self.pq[max_index]
        self.size -= 1
        return self.pq[self.size]

q = ArrayBasedPriorityQueue()
q = MaxHeap()
q.insert(5)
q.insert(10)
q.insert(3)

print(q.getMax())
print(q.getMax())
q.insert(2)
q.insert(15)
q.insert(3)
print(q.getMax())
