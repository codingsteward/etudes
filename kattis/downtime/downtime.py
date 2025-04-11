import math
n, k = (int(i) for i in input().split())
timestamps = [int(input()) for i in range(n)]

# loop through group requests that are within 1000, if the count exceeds k
# then it means i need more than one server

# sliding it let's go
left = 0
max_concurrent = concurrent = 0
for right in range(len(timestamps)):
    concurrent += 1
    while timestamps[right] - timestamps[left] >= 1000:
        concurrent -= 1
        left += 1
    max_concurrent = max(concurrent, max_concurrent)

print(math.ceil(max_concurrent/k))
