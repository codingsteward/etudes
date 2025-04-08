s = input()

def repetitions(s: str) -> int:
    """Find longest substring of single character"""
    longest_rep = 1
    c = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == c: # same as prev, increase counter
            count += 1
        else:
            longest_rep = max(longest_rep, count)
            count = 1
            c = s[i]
    return max(longest_rep, count)


def judge():
    test_cases = {
            'tc': ('abcd', 1),
            'tc1': ('abbcccdddd', 4),
            'tc2': ('1', 1),
            'tc3': ('aaabbb', 3)
            }
    for key in test_cases:
        s, expected = test_cases[key]
        assert(repetitions(s) == expected)
print(repetitions(s))
