# https://codeforces.com/problemset/problem/71/A
# A. Way Too Long Words

N = int(input())
for i in range(N):
    word = input()
    if len(word) > 10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)
