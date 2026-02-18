# https://codeforces.com/problemset/problem/546/A
# A. Soldier and Bananas

k, n, w = tuple(int(i) for i in input().split())
total = 0
for i in range(w):
    total += (i+1)*k
print(total-n if total > n else 0)
