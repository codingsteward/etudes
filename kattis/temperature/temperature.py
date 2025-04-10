X, Y = (int(i) for i in input().split())

# let's say the temperature to reach is Z
# to reach Z in scale B, we need to add Y * Z to X
# and Y *Z + X = Z
# Z(Y-1) = -X
# Z = -X/(Y-1)

if Y-1 == 0:
    if X == 0:
        print("ALL GOOD")
    else:
        print("IMPOSSIBLE")
else:
    print(f"{-X/(Y-1):.6f}")
