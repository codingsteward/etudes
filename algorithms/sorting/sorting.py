# Sorting
def selection_sort(A: list[int]) -> None:
    "Maintain sorted array at the end, find max and swap rightwards"
    for i in range(len(A)-1, -1, -1):
        m = i
        for j in range(i-1, -1, -1): # find max left of i
            if A[m] < A[j]:
                m = j
        A[m], A[i] = A[i], A[m]

A = [5, 3, 4, 6, 1, 7 ,3, 2]
print(selection_sort(A))
print(A)
A.reverse()
print(A)
selection_sort(A)
print(A)


def insertion_sort(A: list[int]) -> None:
    for i in range(1, len(A)): # assume sorted A[:i]
        # expand the array to i, swap leftwards till sort
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1

A = [5,4,3,1,2,3,4,5,6]
insertion_sort(A)
print(A)


def merge_sort(A: list[int], a = 0, b = None) -> None:
    if b is None:
        b = len(A)
    if b-a <= 1: # subarray of length 1 or less is sorted
        return

    c = (a+b+1) // 2 
    merge_sort(A, a, c)
    merge_sort(A, c, b)

    L, R = A[a:c], A[c:b]
    i, j = 0, 0
    while a < b:
        if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
            A[a] = A[i]
            i += 1
        else:
            A[a] = A[j]
            j += 1
        a += 1

A = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]




