# https://codeforces.com/problemset/problem/977/A
# A. Wrong Subtraction

n, k = tuple(int(i) for i in input().split())

for i in range(k):
    if n%10 == 0:
        n //= 10
    else:
        n -= 1

print(n)
