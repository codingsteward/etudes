N = int(input())
A = [int(i) for i in input().split()]
pivots = 0
stack = []
min_array = []
max_array = []

largest = float('-inf')
for num in A:
    max_array.append(largest)
    largest = max(largest, num)
smallest = float('inf')
for i in range(len(A)-1, -1, -1):
    min_array.append(smallest)
    smallest = min(smallest, A[i])

min_array.reverse()
for i in range(len(A)):
    if A[i] > max_array[i] and A[i] < min_array[i]:
        pivots += 1
print(pivots)
