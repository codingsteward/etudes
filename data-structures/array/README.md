# Array

An array is stored as a contiguous sequences of bytes in memory.

Most programming languages require each element of a particular array to be the same size. 


## Matrices

We represent matrix by one or more one-dimensional arrays. Two most common ways to store a matrix are row-major and column-major order.

In row-major order, the mxn matrix is stored row by row. In col-major order, the matrix is stored col by col. 

To store in a single one-dimensional array, M[i, j], the element at row i and col j, the array index = s + (n(i-s)) + (j-s)

[1, 2, 3]
[4, 5, 6] to [1, 2, 3, 4, 5, 6]




## Sequence interface

Python sequence interface 

collections.abc.Sequence
1. __len__ and __getitem__(key)

Fixed array interface
1. build(x)
2. get at (i), set at (i)

No interface provided for adding or not. The array size is fixed based on the x passed in



