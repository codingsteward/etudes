N = int(input())
nums = [int(i) for i in input().split()]

def min_cost(nums):
    if all(num == nums[0] for num in nums):
        return 0
    smallest, largest = min(nums), max(nums)
    min_cost = float('inf')
    for guess in range(smallest, largest+1):
        cost = 0
        for num in nums:
            cost += (num-guess)**2
        min_cost = min(min_cost, cost)
    return min_cost

print(min_cost(nums))
