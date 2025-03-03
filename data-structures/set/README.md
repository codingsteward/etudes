# Sets


## Set interface
Maintain a set of keys having unique keys 

Container
1. Build
2. len

Static
1. find(k)

Dynamic
1. insert(x)
2. delete(k)

Order
1. iter order
2. find min, max
4. find prev, next

Special case interface:
Dictionary, set without order operations
| Underlying    | Container| Static  | Dynamic       |          Order                |
| Data structure| Build (A)| find(k) | insert/delete | find min/max | find prev/next |
| ------------- | -------- | ------- | ------------- | ------------ | -------------- |
| Array         | O(N)     | O(N)    | O(N)          | O(N)         | O(N)           |
| Sorted array  | O(NlgN)  | O(lgN)  | O(N)          | O(1)         | O(lgN)         |


Storing items in sorted keys allow faster find(k) and fid min/max/prev/next
1. min/max at ends of array
2. prev/next/find at lg N via binary search


