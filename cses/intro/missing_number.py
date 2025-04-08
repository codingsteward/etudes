n = int(input())
nums = [int(i) for i in input().split()]

def missing_numbers(nums, n):
    expected = (n+1)*n/2
    return int(expected - sum(nums))

def judge():
    """Run a series of test cases"""
    test_cases = {
            'tc': (5, [2, 3, 1, 5], 4),
            'tc1': (5, [1, 2, 3, 4], 5),
            'tc2': (5, [2, 4, 1, 5], 3),
            'tc3': (5, [4, 3, 1, 5], 2),
            'tc4': (1, [], 1),
            }
    for key in test_cases:
        n, nums, expected = test_cases[key]
        assert(missing_numbers(nums, n) == expected)
judge()

print(missing_numbers(nums, n))
