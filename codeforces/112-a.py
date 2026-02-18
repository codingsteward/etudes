# https://codeforces.com/problemset/problem/112/A
# A. Petya and Strings

s1 = input()
s2 = input()

def compare(s1, s2):
    for i in range(len(s1)):
        if s1[i].lower() < s2[i].lower():
            return -1
        elif s1[i].lower() > s2[i].lower():
            return 1
    return 0

print(compare(s1, s2))
