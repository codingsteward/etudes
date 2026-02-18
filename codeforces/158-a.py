# https://codeforces.com/problemset/problem/158/A
# A. Next Round

n, k = tuple(int(i) for i in input().split())
nums = list(int(i) for i in input().split())
ans = 0
for num in nums:
    if num > 0 and num >= nums[k-1]:
        ans += 1
print(ans)


