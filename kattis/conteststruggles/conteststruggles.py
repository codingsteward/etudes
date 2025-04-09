n, k = [int(i) for i in input().split()]
d, s = [int(i) for i in input().split()]

total_s = s * k
total_d = n * d

total_remaining_avg = (total_d - total_s) / (n-k)
if total_remaining_avg < 0 or total_remaining_avg > 100:
    print("impossible")
else:
    print(f"{total_remaining_avg:.7f}")
