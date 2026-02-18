p, a, b, c, d, n = (int(i) for i in input().split())
import math

# max decline is basically largest to smallest of the values
# decline must be from smaller k to larger k
# so i need to buy earlier, sell later

# to have a biggest decline, buy largest, sell

diff = 0
largest= p * (math.sin(a + b) + math.cos(c + d) + 2)
for i in range(2, n+1):
    curr = p * (math.sin(a*i + b) + math.cos(c*i + d) + 2)
    largest = max(largest, curr)
    diff = max(diff, largest-curr)

print(f"{diff:.9f}")
