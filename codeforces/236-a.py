# https://codeforces.com/problemset/problem/236/A
# A. Boy or Girl

s = input()

chars = set(s)
print("CHAT WITH HER!" if len(chars) % 2 == 0 else "IGNORE HIM!")
