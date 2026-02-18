P = int(input())
for i in range(P):
    K, *A = [int(i) for i in input().split()]
    count = 0
    for j in range(1, len(A)):
        for k in range(j-1, -1, -1):
            if A[k+1] < A[k]:
                A[k], A[k+1] = A[k+1], A[k]
                count += 1
            else:
                break
    print(K, count)


