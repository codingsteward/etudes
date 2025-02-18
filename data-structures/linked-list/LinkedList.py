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
        class_name = type(self).__name__
        return f"{class_name}(item={self.item!r}, next={self.next!r})"

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

