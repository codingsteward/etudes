# Priority queue

A data structure supports operations of inserting a new element and deleting the largest element.

Operations
1. Construct a priority queue from N given items
2. Insert a new item
3. Remove the maximum item
4. Change the priority of an arbitrary specified item
5. Remove an arbitrary specified item
6. Join two priority queues into one large one

Duplicate keys: any record with largest key value

## Elementary implementations

### Unordered Array as underlying data structure

Find max operation: Linear scan array to find largest, swap with last item and decrement queue size

Insertion operation: Append to back of array determined by current size

Insert: O(1), append to back
Remove maximum: O(N), linear scan to find largest
Remove: O(1), pop from back
Find maximum: O(N), linear scan to find largest
Change priority: O(1), update array index by key
Join: O(N), basically extending an array

### Exercises

1. Implement PQ using ordered array
2. Implement PQ using unordered linked list
3. Implement PQ using ordered linked list

### Heap data structure

A tree is heap-ordered if the key in each node is larger than or equal to the keys in all of that node's children. Equivalently, key of each node is smaller than or equal to key in node's parent.

No node in a heap ordered tree has a key larger than the key at root.

A heap is a set of nodes with keys arranged in a complete heap-ordered binary tree, represented as an array.

Parent of node i = floor(i/2)
Children of node i = 2i and 2i + 1

Complete tree allow us to use a compact array representation where we can get to parent and children without needing to maintain explicit pointers.

### Algorithms on heaps

Make a simple modification that violate heap condition, traveling through the heap, modifying the heap to ensure heap condition is satisfied everywhere. This process is called heapify.

Two cases: priority of node is increased, new node is added at bottom of heap. Travel up the heap to restore heap condition.

Priority is decreased or replace node at root, travel down the heap.

### Time complexity

Insert operation: No more than lg N comparisons
Remove max operation: No more than 2 lg N comparisons

Both operation moves along a path from root to bottom of heap. No path in a heap of size N is more than lg N. Remove max requires two comparison for each node.
1. One to find larger child
2. One to decide whether to promote a child


Change priority, remove, replace max operations can be all implemented with a heap s.t no more than 2 lg N comparisons required.

### Replace the maximum
Push replaced element on back of array.

Use heap[0] for elegant solution

### Change priority
Remove object, reinsert it.
Change priority of object, run heapify.

### Combining two priority queue



### kth largest of N items

1. Build a heap, remove K largest elements
2. Build a min-heap of size k. Replace min(insert, remove) for remaining elements

https://algs4.cs.princeton.edu/24pq/


