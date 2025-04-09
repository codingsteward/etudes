wc, hc, ws, hs = (int(i) for i in input().split())

if ws <= wc-2 and hs <= hc -2:
    print(1)
else:
    print(0)
