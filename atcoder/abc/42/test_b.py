N, L = (int(i) for i in input().split())

strings = [input() for i in range(N)]
strings.sort()
print("".join(strings))

