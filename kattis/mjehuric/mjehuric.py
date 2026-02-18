A = [int(i) for i in input().split()]

for i in range(len(A)-1, -1, -1):
    for j in range(i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            print(" ".join(str(i) for i in A))

