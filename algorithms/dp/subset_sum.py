

# Does a subset with target sum exists?
# loop through the array, it can be part of it or not

# recursive relationship? 
# substack_sum(i, s) => substack_sum(i-1, s) or substack_sum(i-1, s-nums[i])

# Given a set of integers, determine if there's a subset that sums to target

# can DP on the array index
# or DP on the ??

def substack_sumx(nums, target): # return true if subset sums to target
    if target > sum(nums) or target < 0:
        return False
    if target == 0: return True

    return substack_sumx(nums[1:], target) or substack_sumx(nums[1:], target-nums[0])


def subset_sum(nums, target):
    # ?? 
    # DP version??
    if target > sum(nums) or target < 0:
        return False
    
    # dp[i][s] = can achieve sum s using up index i elements
    dp = [[False] * (target+1) for _ in range(len(nums)+1)]

    for i in range(len(nums)+1):
        dp[i][0] = True

    # bottom up DP
    # dp[i][s] = dp[i-1][s] or dp[i-1][s-nums[i]]
    for i in range(1, len(nums)+1):
        for s in range(target+1):
            dp[i][s] = dp[i-1][s]
            if s >= nums[i-1]:
                dp[i][s] = dp[i][s] or dp[i-1][s-nums[i-1]]

    return dp[len(nums)][target]


arr1 = [3, 34, 4, 12, 5, 2]
target1 = 3+4+12+2

print(subset_sum(arr1, target1))
print(substack_sumx(arr1, target1))

def test_subset_sum():
    # Test 1: Basic case
    assert subset_sum([3, 34, 4, 12, 5, 2], 9) == True  # 4 + 5 = 9
    
    # Test 2: No solution
    assert subset_sum([3, 34, 4, 12, 5, 2], 30) == False
    
    # Test 3: Single element
    assert subset_sum([5], 5) == True
    assert subset_sum([5], 3) == False
    
    # Test 4: Target is 0 (empty subset)
    assert subset_sum([1, 2, 3], 0) == True
    
    # Test 5: All elements needed
    assert subset_sum([1, 2, 3], 6) == True
    
    # Test 6: Large numbers
    assert subset_sum([100, 200, 300], 500) == True  # 200 + 300
    
    # Test 7: Duplicate elements
    assert subset_sum([2, 2, 2], 4) == True  # 2 + 2
    
    print("✓ All subset sum tests passed!")

test_subset_sum()
