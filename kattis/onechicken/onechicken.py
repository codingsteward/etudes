N, M = (int(i) for i in input().split())
pieces = "pieces" if abs(N-M) > 1 else "piece"
if N < M:
    print("Dr. Chaz will have %d %s of chicken left over!" % (M-N, pieces))
else:
    print("Dr. Chaz needs %d more %s of chicken!" % (N-M, pieces))
