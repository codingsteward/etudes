# Atcoder ABC 046

## Task A AtCoDeer and Paint cans

Straight forward check if 3 integers, or count distinct

first mistake
1. int(a != b) + int(a != c + int(b != c) was wrong
2. 3 5 5 would give 1 + 1 + 0 = 2 ok
3. 3 5 7 would give 1 + 1 + 1 = 3 ok
4. 3 3 3 would give 0 + 0 + 0 = 0 wrong

## Task B Painting balls with AtCoDeer

Number of ways to paint balls with same color adjacent each other

SOunds like a DP problem

num ways (i, prev) = num ways(i+1, new color) for color != prev

num ways(end, prev) = k-1

helper(0, None) = helper(1, 0) + helper(1, 1)
= helper(2, 1) + helper(2, 0)
= 1 + 1

Bug 1: starting i = 0 and ending at i == N means counting twice. paint the ith ball = 0 and ith ball = 1 for k-1 times

To fix, start at 1


TLE: recursion is off, should have DP

dp(i, k) refers to number of ways to paint ball i with color k ?

dp(i, k) = sum of dp(i-1, k') across all k' != k

final answer is dp(N, k) across all k

## Task C


## Task D



