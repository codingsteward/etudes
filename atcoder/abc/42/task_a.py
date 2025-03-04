inputs = (int(i) for i in input().split())

count_5 = count_7 = 0
for x in inputs:
    if x == 5:
        count_5 += 1
    elif x == 7:
        count_7 += 1

print("YES" if count_5 == 2 and count_7 == 1 else "NO")
