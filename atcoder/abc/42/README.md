Contest main link: https://atcoder.jp/contests/abc042

This is mainly practice for me to learn and solve

# Task A

a, b, c = (int(i) for i in input().split())

Conditionals

# Task B

Lexicographically smaller strings means there's index i where any index j < i, s[j] == t[j] and s[i] < t[i]

To solve this, the smallest string will then have the smallest s[i] at index 0, the next smaller at index 1 and so on.

Sort strings, concat


# Task C

Find the smallest number that doesn't contain digits D1, D2, ... , DK and is at least N

I guess to form N with remaining digits.

Find the smallest digit to replace the first digit

If it's equal, then find smallest to replace second digit etc...


How to construct the number?
Loop through it.

For first digit, it's digit * (...) + digit * (...) etc..

if len(digit) = 3
    first digit is 100 place or 10^2
    second digit is 10^1

Given index i, the "places" is 10**(len(N)-i-1)

The amount of edge cases is quite surprising... I found a lot of errors luckily. Lots of bugs... maybe over 5-10 of them. I should keep track of these bugs because it's a good source of learning. Not to make these errors again. 

Errors
1. Available digits exclude 9 because range(9) instead of range(10)
2. Did not handle edge case where first digit is 9 and no digit can replace it
3. Did not handle edge case where first digit is 9 and first smallest digit is 0
4. For first digit is 9, I multiplied the smallest digit by 10 to power (N-1) but since its one place to the right, as we overflow the 9, it should be power(N) instead



# Task D


Looks like graph traversal in matrix, DP

num ways (i, j) = num ways (i-1, j) + num ways (i, j-1)

To enter a square, can only come from left or top

Might have some optimisations to skip forbidden squares (A rows, B columns)


Bugs 1:
1. If r >= H-A or c < B 
    - Should be AND because only target those rows and columns 
2. For 1D DP space complexity, should start from row range(1, H) instead of starting at 0
3. dp[c] += dp[c-1] cannot take if c-1 < B

Time complexity gap:
1. Iterating the entire matrix is too slow
    - Tried to optimise by restricting col start
    - Still too slow, turns out allocate matrix already failed
2. Optimise space complexity
    - Since each iteration depends on the row before you, in theory i should only have 1 row for DP

Wow, this is way more difficult.. apparently DP is still too slow. I think math combinatorics might work.

Also, I got WA for question 3 l o l after lots of debugging.


## Redo'ing task C

I got WA for task C because the "greedy"/naive approach didn't work out.

Found a test case N = 529, available digits = {5, 2}
At digit 9, since I need bump it up, it overflows to digit 2. Digit 2 becomes 3. But 3 is not available, and so is 4, 5, 6 ... 9. Then I need bump up again. And so on.

End of the day it rolls to 2000

Bug 1:
1. Return N instead of guess

Bug 2:
1. Test case still fails..
2. guess > 0 is wrong, it's guess != 0 i.e when guess = 0 then end


## Finishing task D

Combinatorics..

Given there are W moves and H moves, total of W+H

The number of ways to reach from top left to bottom right is hence (W+H) choose (W)

We compute the number of ways right before the forbidden rows

Then from restricted column, we compute downwards to rightmost

Even though I copied some code over, feels like it wasn't enough. Apparently there's a fast factorial mod p calculation compared to purely factorial.

The number theory behind it I'm unfamiliar and probably will take some time to learn next time...


