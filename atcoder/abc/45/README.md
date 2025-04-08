# ABC 045

## Trapezoid

calculate the area is basically 

one rectangle of a * h 
triangle of 1/2 * 2 * (b-a) * h

1/2 * b1 * h + 1/2 * b2 * h

b-a * h + a * h = b * h ?

when is it (a+b)* h/2 ? 

0.5 x (b-a) x h + (a) * h

(b+a)h / 2

## Card game for 3

Pure simulation should work

whichever pointer reaches end of string first wins

## Many formulas

Feels like a backtracking problem

Try all possible insertions, evaluate it

Bound is 10

so 2^(n-2) is ok

Why divide by 2 though??


## Snuke's coloring

Naive is to compute all 3x3 rectangles.. but given H, W are 10^9, it's too large to try all

If I have the count of each 3x3 black squares, then it will be manageable.

Maybe the trick is when i'm adding each square, i need to update the count for each 3x3 black squares


