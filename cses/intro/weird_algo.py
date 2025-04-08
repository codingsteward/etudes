n = int(input())

def weird_algo(n):
    ans = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n*3) + 1
        ans.append(n)
    return ans

def judge():
    """Run a series of test cases"""
    test_cases = {
            'tc1': [1, [1]],
            'tc2': [2, [2, 1]],
            'tc3': [3, [3, 10, 5, 16, 8, 4, 2, 1]],
            'tc4': [4, [4, 2, 1]],
            'tc5': [5, [5, 16, 8, 4, 2, 1]]
            }
    for key in test_cases:
        n, expected = test_cases[key]
        assert(weird_algo(n) == expected)

print(*weird_algo(n))
