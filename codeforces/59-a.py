# https://codeforces.com/problemset/problem/59/A
# A. Word

s = input()
lower = 0
for c in s:
    if c.islower():
        lower += 1

if len(s)-lower > lower:
    print(s.upper())
else:
    print(s.lower())
