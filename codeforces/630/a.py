n = int(input())

a = 5
res = 1
while n > 0:
    if n & 1:
        res = res * a % 100
    a = a * a % 100
    n >>= 1
print(res)
