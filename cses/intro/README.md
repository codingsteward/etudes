# CSES problem sets

Tackling the intro problems for now


I think start with a base first, then move up slowly

For every problem I should aim to test its correctness by coming up with suitable test cases

I should also be able to identify the time/space complexity correctly.

I should not submit the code until I come up with at least 10 test cases or X number of independent test sets

There's no submitting of code, just test your own..

## Weird algorithm

Algorithm
Simulation

Test cases
1. Test odd and even number
2. test 1 itself 


## Missing number

Since n = 10^5, try count all in bit array

the one bit not set is the one

The other approach is math

1. 1 to N total sum is X
2. if sum(nums) != x then what's missing is that digit

sum 1 to N is ?

(n+1)(n)/2

## Repetitions

Find longest repetition in a sequence i.e maximum length substring of single type of char


Can use groupby in python, then run max

or just linear scan and keep track

Test cases:
1. Single char string
2. Multi char equal length
3. longest length at end
4. single char string


## Increasing array

Minimum moves => increase till as much as prev

Be careful, after increase, need update array so future will also increase if it's smaller

[5, 1, 1] = [5, 5, 1] = [5, 5, 5]


## Permutations

Beautiful if difference not 1 for adjacent

Construct by odd numbers first, even second

2 and 3 are not possible

rest are possible

Odd numbers first is wrong. Should have printed even first

1 3 2 4 

## Number spiral

Was kinda difficult.. after drawing a few out. Realise like within a box, it's n^2 of numbers 

Then, at the edges, you can tell the start number based on what's the row/column

for example, column 4 i.e 5 columns => ends with 25 
    and goes down in descending


column 5, then starts with column4+1, then goes on ascending

row start is 16, then descending
Same concept


if r <= c, i should look at column number and count

if r > c, start at row and count from left to right


## Two knights

Find how many ways can place 2 knights

If simulate all possible, will be too large
For each knight placement, find out which position next knight should be that it will hit it

for each knight position, it has up to 8 unique slots

loop nxn, find out how many pos other knight in the 8 unique slots

add nxn-1-unique slots

every row is the same right, after it's in the middle with no boundaries to worry about

Bug 1: trivial c-1 should have been c+1

TLE: looks like it's too slow

I'm also recomputing the board over and over again

When incrementally, board kxk and k+1 x k+1 only introduces one more column and row into the picture

so i should focus on that instead

So kinda gave up... turns out it's a math formula. counting the number of 2x3 and 3x2 blocks for the knight attacks

## Two sets

To be able to split equally, means the total sum is even

then just find out what add up to sum//2 ?

1 2 3 4 5 6

(16), (25) (34)


let's say we got two sets of equal sums = X

now we add a new number N

to fit N into one of the set, one set need to give up N worth to the other set to keep things balance

to keep things balance

12345678

(18), (27), (36), (45)

9 ? 

123456789

19 28 37 46 5

1 2 3 4 5 6 7 8 9 10 11 => 66, l

12 * 11 / 2 = 66

1, 11
2, 10
3, 9
4, 8
5, 7


