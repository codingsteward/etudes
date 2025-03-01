# Sorting

## Selection sort

Already maintained a sorted array at the end, find the max element to the left and swap it

## Insertion sort

Already maintained sorted array at the start, sort the next element by swapping leftwards until right position


Both selection and insertion sort are in-place algorithms i.e they do not need additional space.

Insertion sort is stable i.e items having the same value will appear in sort the same order as they appeared originally.

## Merge sort

Algorithm divides the array into half and recursively run merge sort on it. Then, it takes the sorted two halves and merge into one array.

Array of length 1 is sorted.

There exists in-place merge sort but the algorithm is quite complicated


