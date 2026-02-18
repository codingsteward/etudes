# task d
from collections import Counter

H, W, N = (int(i) for i in input().split())
painted = []
for i in range(N):
    painted.append((int(i)-1 for i in input().split()))

# for each painted cell, it could contribute to 9 possible boxes
# so there will be 9N possible rectangles
total = (H-2) * (W-2)
counter = Counter()
for a, b in painted:
    # a,b will be involved up to 9 possible different 3x3 subrectangle
    # ...?
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_a, new_b = a+i, b+j
            if 0 <= new_a < H and 0 <= new_b < W:
                # valid subrectangle??
                if new_a == 0 or new_a == H-1: continue
                if new_b == 0 or new_b == W-1: continue
                counter[(new_a, new_b)] += 1

ans = [0]*10
# rectangles with 0 = total rectangles - rectangles with painted
for k,v in counter.items():
    ans[v] += 1
    total -= 1
ans[0] = total
for i in range(len(ans)):
    print(ans[i])
