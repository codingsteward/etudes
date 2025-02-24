# Linked list

## Singly linked list
Linked list is either empty or contains data item and a link to the next node.


## Doubly linked list
Doubly linked list is similar to a linked list with an addition back pointer "prev" to point to the previous node. This allows the doubly linked list to traverse forward and backward.


## Core stuff to know

Advantages of linked list: memory allocation, fast insertion/removals
1. Index out of bounds don't occur
2. Insertion and deletion are simpler/faster
3. Moving pointers is easier than moving items itself
Disadvantages of linked list: no indexing access in O(1)
1. Linked structures require extra memory for storing pointers
2. No efficient random access in arrays
3. Less better memory locality and cache performance compared to random pointer jumping

[] Define a LinkNode
[] Linked list processing
- [] Insertion, removal
- [] Reversing
- [] Insertion sort
- [] Use of sentinel nodes in head/tail
- [] Traversing a linked list
[] Searching a linked list
[] Find kth node from front or back
[] Circular list (Josephus problem)
- [] Array representation of circular list
[] Doubly linked list


## CtCi problems

1. Runner technique i.e slow/fast pointers

Questions
1. Remove duplicates from unsorted linked list
    - Temporary buffer is not allowed
2. Find kth to last element of linked list
3. Delete middle node
4. Partition linked list around a value x s.t all nodes less than x come before all nodes greater and equal to x
5. Given numbers stored in a linked list, sum numbers and return in linked list
6. Check if linked list is palindrome
7. Determine if two lists intersects
8. Find the start node of the cycle

## EPI problems

Questions
1. Merge two sorted lists
2. Reverse a single sublist from i to j
    - Reverse group of k nodes at a time
3. Test for cyclicity 
4. Test for overlapping list i.e intersection
    - Overlapping list if they might have cycles
5. Deleting a node in O(1)
6. Remove kth last element from a list
7. Remove duplicates from a sorted list
8. Implement cyclic right shift
9. Implement even-odd merge
10. Test if palindrome
11. Implement list pivoting i.e partition
12. Add numbers represented in lists (msb comes first or last)

