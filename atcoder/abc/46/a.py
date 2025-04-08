# Task A
a, b, c = (int(i) for i in input().split())

uniques = set([a, b, c])
print(len(uniques))
