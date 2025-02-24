from LinkedList import LinkedNode

class SinglyLinkedList:
    """
    Implements fundamental helper methods on linked list such as insertion, removal etc
    """
    
    def __init__(self, iterable=None):
        if iterable:
            self.makeList(iterable)
        else:
            self.head = None
            self.count = 0

    def makeList(self, iterable):
        curr = sent = LinkedNode(None)
        for item in iterable:
            curr.next = LinkedNode(item)
            curr = curr.next
        self.head = sent.next
        self.count = len(iterable)

    def __len__(self):
        return self.count

    def append(self, x):
        new_node = LinkedNode(x)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
           self.head = new_node

    def appendLeft(self, x):
        new_node = LinkedNode(x)
        if self.head:
            new_node.next = self.head.next
            self.head = new_node
        else:
            self.head = new_node

    def pop(self):
        '''Removes an element from the end of list. Raise IndexError if the list is empty
        >>> xs = SinglyLinkedList([1, 2, 3])
        >>> xs.pop()
        [3]
        '''
        if self.count == 0: raise IndexError('no elements present')
        if self.count == 1:
            res = self.head
            self.head = None
        else:
            curr = self.head
            while curr.next and curr.next.next:
                curr = curr.next
            res = curr.next
            curr.next = None
        return res

    def reverse(self):
        pass


    def middle(self):
        '''Middle will iterate to the middle node and return it
        In the case of even length lists, return the second middle
        >>> xs = SinglyLinkedList([1, 2, 3])
        >>> xs.middle()
        [2, 3]
        >>> xs = SinglyLinkedList([1, 2, 3, 4])
        >>> xs.middle()
        [3, 4]
        '''
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


