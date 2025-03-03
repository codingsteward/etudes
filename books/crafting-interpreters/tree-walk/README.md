# Lox Language

// First lox program
print "Hello, world!";

Lox's syntax is a member of C family.

Languages that are small but useful => high level "scripting language" like JS or Scheme.

Dynamic typing
1. Variables can store values of any type. Error is detected and reported at runtime
2. A static type system is a ton of work to learn and implement.


Automatic memory management
1. Reference counting
    - Count number of references for each object, if reach 0, garbage.
    - Problems: cycles (two objects refer to each other)
    - Space overhead: store reference count
    - speed overhead
    - not real time
2. Tracing garbage collection
    - define reachability of objects
    - Trace through working set of memory

Naive mark and sweep:
1. each object has a flag
2. step 1: tree traversal from root and mark each reachable with "in-use"
3. step 2: sweep to examine free blocks those mark "not in use" are freed

Disadvantages:
1. entire system suspended, no mutation of working set allowed
2. real-time not allowed

tri-color marking
1. white: condemend set to recycle memory
2. black: no outgoing edge to white and reachable by root
3. grey: reachable by root, not yet scan if reach white

Algo
1. pick 1 from grey set
2. move each white object referenced by it to grey set
3. move 1 to black set 
4. repeat until grey empty

## Data types

Booleans: true, false
Numbers: double-precision floating point (integer or decimal literals)
strings
nil or null

## Expressions

Arithmetic
1. add, subtract, multiple, divide

Comparison and equality
1. <, <=, >, >=, ==

Logical operators
!, and, or

Precedence and grouping
()

## Statements
Expression job is to produce a value. Statement job produce an effect.

Adding ; to expression makes it a statement.
## Variables

Declare variables using var statements.

## Control flow

if statement, whilte loops, for loops

## Functions

makeBreakfast()

define a function with fun printSum
