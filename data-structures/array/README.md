# Array

An array is stored as a contiguous sequences of bytes in memory.

Most programming languages require each element of a particular array to be the same size. 


## Matrices

We represent matrix by one or more one-dimensional arrays. Two most common ways to store a matrix are row-major and column-major order.

In row-major order, the mxn matrix is stored row by row. In col-major order, the matrix is stored col by col. 

To store in a single one-dimensional array, M[i, j], the element at row i and col j, the array index = s + (n(i-s)) + (j-s)

[1, 2, 3]
[4, 5, 6] to [1, 2, 3, 4, 5, 6]


