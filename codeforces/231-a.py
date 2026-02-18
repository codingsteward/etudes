# https://codeforces.com/problemset/problem/231/A
# A. Team
n = int(input())
ans = 0
for i in range(n):
    arr = [int(j) for j in input().split()]
    if sum(arr) >= 2:
        ans += 1
print(ans)
