n = int(input())
nums = [int(i) for i in input().split()]

def increasing_array(nums):
    incr = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            incr += nums[i-1] - nums[i]
            nums[i] = nums[i-1]
    return incr
def judge():

    test_cases = [
            ([5, 1, 1], 8),
            ([3, 2, 5, 1, 7], 5),
            ([1], 0),
            ([1, 2, 3, 4, 5], 0),
            ([5, 4, 3, 2, 1], 10),
            ]
    for nums, expected in test_cases:
        assert(increasing_array(nums) == expected)
print(increasing_array(nums))

