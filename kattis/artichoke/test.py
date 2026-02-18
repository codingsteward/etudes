import math
p,a,b,c,d,n = [int(x) for x in input().split()]
pricearray = []
maxval = p*(math.sin(a+b)+math.cos(c+d)+2)
i=2
bigdiff = 0
while i <= n:
    val = p*(math.sin(a*i+b)+math.cos(c*i+d)+2)
    if maxval < val:
        maxval= val
    elif maxval-val > bigdiff:
        bigdiff = maxval-val
    i += 1
print(bigdiff)
