# https://codeforces.com/problemset/problem/263/A
# A. Beautiful Matrix

for i in range(5):
    row = list(int(j) for j in input().split())
    for k in range(5):
        if row[k] == 1:
            print(abs(2-k)+abs(2-i))


