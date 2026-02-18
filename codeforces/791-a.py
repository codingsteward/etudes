# https://codeforces.com/problemset/problem/791/A
# A. Bear and Big Brother

a, b = tuple(int(i) for i in input().split())

years = 0
while a <= b:
    years += 1
    a *= 3
    b *= 2
print(years)
