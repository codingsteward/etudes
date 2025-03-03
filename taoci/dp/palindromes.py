# Contains numerous DP subroutines specifically on palindrome
# Main palindrome recurrence
# Palindrome is a palindrome if s[i] == s[j] and s[i+1, j-1] is a palindrome
# Put in another way, a length 1 substring is a palindrome. 
# Length 3 substring is a palindrome if s[i] == s[j] and the length 1 substring within is a palindrome
# 

# longest palindrome = 

def is_palindrome(s):
    pass # linear scan

def all_palindromes(s):

    def is_palindrome(s, i, j):
        """Returns true if substring[i:j] is palindrome"""
        if i == j:
            return True
        if i+1 == j:
            return s[i+1] == s[j]
        return s[i] == s[j] and is_palindrome(i+1, j-1)

def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = [0, 0]

    # All length 1 substring s(i, i) is palindrome
    for i in range(n):
        dp[i][i] = True

    # All len 2 substring s(i, i+1) is palindrome
    # If s[i] == s[i+1]
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True

    # Recurrence relationship
    # is_palindrome(i, j) = s[i] == s[j] and is_palindrome(i+1, j-1)

    # Bottom up DP since we have values for length 1 and 2
    # p_len is the incremental length from base case
    # 1 -> 3 -> 5
    # 2 -> 4 -> 6
    # p_len = 2, start from length 3 onwards
    # p_len = 3, start from length 4 onwards
    for p_len in range(2, n):
        for start in range(n-p_len):
            end = start+p_len
            if s[start] == s[end] and dp[start+1][end-1]:
                dp[start][end] = True
                ans = [i, j]
    return ans







