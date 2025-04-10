a, b, c, d ,e = (int(i) for i in input().split())
score = int(input())

if score >= a:
    print("A")
elif score >= b:
    print("B")
elif score >= c:
    print("C")
elif score >= d:
    print("D")
elif score >= e:
    print("E")
else:
    print("F")
