N, C = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]


def dp(n, c):
    # bottom up DP from 0 0 to N/C
    dp = [[1] * c for _ in range(n)]
    print(dp)


# Returns activity level given n kids and c candies
def xdp(n, c):
    # base case?
    # c = 0?, n = 0?, n = 1? c = 1?
    if n == 0: # no kids to distribute
        return 0
    if c == 0: # no candies to distribute, all will be power of 1
        return 1
    if n == 1: # last kid, the candy is all his
        return A[n-1]**c
    # recursive case
    # consider all range to give this particular kid
    total = 0
    for i in range(c+1):
        total += dp(n-1, c-i) * A[n-1]**i
    return total

print(dp(N, C))





