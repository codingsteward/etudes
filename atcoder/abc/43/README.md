# Atcoder Beginner contest 043

## Task A: Children and candies

1 + 2 + 3 + ... + N => AP sum

(1+N) * N // 2 

## Task B: Unhappy hacking

3 keys, 0, 1 and backspace

0 => add 0 after the string
1 => add 1 after the string
backspace => if string empty, nothing; rightmost of string is deleted

s => keystrokes => map to final string

Stack problem.

We want to remove the rightmost character fast. 

## Task C: Be together

N integers a1, a2, a3 ... an

Transform each integer s.t there are N equal integers

Transforming an integer from x to y: costs (x-y)^2

Each integer has to be transformed separately. 

Find the minimum cost to make all N equal.



For every integer A, try to make every other integer B to be equal to A. Find minimum out of all of them.

This is O(N integers * N-1 integers) = O(N^2)

To minimize the cost (x-y)^2 => this means the abs diff between x and y should be as close as possible

Suppose we can find this final integer, computing the cost is easy.

1st question: would the final integer be in the list?

(x-(y+1)^2 = (x-y+1)^2 = x^2 - xy + x -xy + y^2 -y + x - y + 1 = x^2 - 2xy + 2x +y^2 -2y + 1

(x-y)^2 = x^2 - xy -xy + y^2 = x^2 - 2xy + y^2

this turns out to be an additional 2x-2y+1 in cost

2(x-y)+1

if y is smaller than x, then by increasing y, we pay a higher price

if y is larger than x, then by increasing y, we pay a smaller price 

Naive way: try all integers doesn't work. The final integer might not be in list.

### I know if we use a smaller final number than smallest or bigger final number than biggest, it will cost more

converting to the smallest is better than convert to smallest -1 since we need to pay more

Same for biggest.

So I know the final number is a range between smallest and biggest

Since the max diff is 100 - (-100) = 200
200 * 100 * 100 = 2 * 10^6 still manageable


## Task D: Unbalanced

string t is unbalanced if and only if length of t >= 2 and more than half letters are same

Find if there's unbalanced substring within a string

No need to be longest etc..


### Initial thoughts

Thought sliding window...?

The thing is there are different characters, so most of them might not have majority.

Sliding window means expand a substring rightward but I don't know whether to stop or continue.

Prefix sums?

Was thinking of trying every character

From first occurrence expand to last occurrence

If this is the majority element, then there exist a substring from first element onwards to the last.

s abcd s b s d s

sliding window each character

if s then a, then they cancel out each other 
so we don't have to include sa in the substring


Bug 1:
1. Use ascii letter instead of lowercase

Bug 2:
1. Included substrings that started with index 0


Bug 3:
1. I thought exclude index 0 but turns out the strings are 1-indexed so i need add 1 to both answers....


I kinda peek at the editorial because I'm just confused why...

Then I felt like the advice is not to look at the editorial.... until I solve it. And it's ok to delay the solving... for a moment.

Still need to clarify when it's the right time to end it though.


So the only possible valid unbalanced strings are XX and XAX. Anything more inbetween XAX will make it balanced.

we don't have to check any longer substrings 


## Reflections

8 WA... this is what costing me in my interviews. A lack of ability to check my own code is ultimately failing me. 
