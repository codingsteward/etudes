a, b, c = (int(i) for i in input().split())
first, second = b-a, c-b
if first > 0 and second < 0 or (first < 0 and second > 0):
    print("turned")
elif first == second:
    print("cruised")
elif abs(second) > abs(first):
    print("accelerated")
elif abs(second) < abs(first):
    print("braked")
