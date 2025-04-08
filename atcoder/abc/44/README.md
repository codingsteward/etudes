# AtCoder 44 ABC

## Task A

X for first k, Y for k+1 onwards

N nights how much =??

If min(N, k), max(N-k, 0)


5 nights, k = 3

1 2 3 4 5

3X + 5-3 = 2Y

First approach: math formula
1. Bug 1: forgot to multiply by Y



## Task B

w is lowercase, beautiful if 
1. each lowercase occurs even times

Approach 1
1. use dictionary to count occurrences

Approach 2
1. use 26 char map to count

Two loops to check frequencies the second time

## Task C

Select 1 or more cards, average is exactly A

How does adding one card affect average?

sum(N)/N

sum(N)+N+1 // (N+1)

sum(N)/(N+1) + X/(N+1)

(n+1) * prev = n * prev + nx

nprev + prev = n  * prev + nx
prev = nx

Average stays the same if prev sum = n * x

or if you add x = averageprev, then stays the same

if you add a larger number, average goes up

if you add a smaller number, average goes down

    4 8 

7 9 8 9

pick 7 or not

seems like a backtracking recursion problem

pick 7 =>

2^50 though??


Approach 1: naive backtracking
1. too slow for large numbers
2. seems like duplicate numbers are multiplying a lot
3. no pruning also

Approach 2: improved backtracking
1. group duplicates together


let's say i have 8 counts of 3

how many ways can i combine this?

prev = 10, count = 2

does it matter if i put

prev = 13, count = 3

vs 

prev = 34, count = 10

prev(10, 2) + prev(13, 1) + prev(...)

sum(nums), N, N

N * N * 50 * N 

50 to power 3 = 125 000 


Approach 3: Try DP

Bug 1:
1. current average > A, i put nums[i] > current average


Failed 7 test cases. As expected, maybe can't scale to 50 yet?

Approach 4: Combining numbers together

given 33 counts of 3

the average is still 3.

but the previous will be scaled down

3 counts of 3, adds a new avg of 3

but previous will be prev / count+3

Given a linear chunk of 33, 3

i just return (prev+3, count+1, i+33) + (prev+6, count+2, i+33) + ... + (prev, count, i+33)

essentially skipping 2**33 stuff?


Approach 5: Use combinations.... didn't thought of it

how many ways to pick 5 cards given N cards

number of ways to pick 1, 2, 3

3 + 2 + 1 = 6 

normal DP.



Approach 6: Although the combinations improvement of duplicate counts was "helpful", it didn't solve shit.

Still TLE.

Actually, it's to do bottom up DP on the same DP array I've created...

top down looks ok but still exponential in terms of branching.


## Task D: Digit Sum













