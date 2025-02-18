class LinkedNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        curr, res = self, []
        while curr:
            res.append(str(curr.item))
            curr = curr.next
        return '['+", ".join(res)+']'

    def __repr__(self):
        return str(self)

class DoublyLinkedNode:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.item)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(item={self.item!s})"

class LinkedList:
    """
    Singly linked list and helper methods
    """
    def __init__(self, arr=None):
        if arr:
            self.head = LinkedList.make_list(arr)
        else:
            self.head = None

    def make_list(arr):
        """
        Create a linked list from a Python list
        >>> xs = LinkedList.make_list([1, 2, 3])
        >>> xs
        [1, 2, 3]
        """
        curr = sent = LinkedNode(None)
        for item in arr:
            curr.next = LinkedNode(item)
            curr = curr.next
        return sent.next

    def append(self, x):
        """
        Add an item to the end of the list
        >>> xs = LinkedList([1, 2, 3])
        >>> xs.append(5)
        >>> xs
        [1, 2, 3, 5]
        """
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = LinkedNode(x)

    def insert(self, i, x):
        """
        Insert an item at given position. xs.insert(0, x) inserts at front of list
        >>> xs = LinkedList([1, 2, 3])
        >>> xs.insert(0, 5)
        >>> xs
        [5, 1, 2, 3]
        >>> xs.insert(1, 4)
        >>> xs
        [5, 4, 1, 2, 3]
        >>> ys = LinkedList([1, 2, 3])
        >>> ys.insert(3, 4)
        >>> ys
        [1, 2, 3, 4]
        """
        if i == 0:
            self.head = LinkedNode(x, self.head)
            return
        curr = self.head
        for _ in range(i-1):
            curr = curr.next
        curr.next = LinkedNode(x, curr.next)

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return str(self.head)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
