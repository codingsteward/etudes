a, b, c = (int(i) for i in input().split('/'))
if a >= 13:
    print("EU")
else:
    if b >= 13: # a <= 12 and b >= 13
        print("US")
    else:
        print("either")
