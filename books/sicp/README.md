# SICP

List of programs that were coded out

## The elements of programming
This chapter defines the language and how it combines simple ideas to form more complex ideas.

- Primitive expressions
- Means of combination
- Means of abstracted

### Naming and the environment

1. Provides using names to refer to computational objects, the name identifies a variable whose value is the object
2. Define is our language's simplest means of abstraction
3. Associating values with symbols means interpreter must maintain memory to keep track of them i.e the global environment

(define size 2)
(define pi 3.14159)
(define radius 10)
(define circumference (* 2 pi radius))

#### Evaluating combinations

To evaluate a combination, do the following
1. Evaluate the subexpressions of the combination
2. Apply the procedure that is the value of leftmost subexpression (operator) to the arguments of the other subexpressions (operands)

Evaluate is recursive in nature. The terminal nodes represent either operators or numbers.

To evaluate primitive expressions:
1. values of numerals
2. values of built-in operators are machine instruction sequences to carry out operations
3. values of other names are objects associated with those name

(define x 3) is not a combination. It's a special form with its own evaluation rule.


#### Compound procedures
Procedure definitions in which a compound operation can be given a name and referred to as a unit
General form of procedure definition:
(define (<name> <formal parameters>) <body> )

E.g, to square a number, (define (square x) (* x x))


#### Substitution model

To evaluate a combination whose operator names a compound procedure, the interpreter follows same process. To apply a compound procedure to arguments, evaluate the body of the procedure with each formal parameters replaced by corresponding argument.

The substituion is accomplished by using a local environment for the formal parameters.

##### Applicative order vs normal order

Applicative: evaluates operators and operands, then applies resulting procedure to resulting arguments (evaluate arguments then apply)

Normal order: Substitute operand expressions until an expression involving primitive (fully expand then reduce)

#### Conditional expressions and predicates

Case analysis using cond

General form:
(cond (<p1> <e1>)
      (<p2> <e2>))

Special form if
(if <predicate> <consequent> <alternative>)

Logical composition operations
(and <e1> ... <en>)
(or <e1> ... <en>)
(not <e>)


#### Newton's method notes
https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

#### Procedures as black box
We are not concerned how the procedure computes its results, only with the fact it computes the result.

A procedure definition should be able to supress detail. A user should not need to know how the procedure is implemented in order to use it.

##### Local names
Meaning of the procedure should be independent of the parameter names used by author. Parameter names of a procedure must be local to the body of the procedure.

A formal parameter is a bound variable. A procedure definition binds its formal parameters.

The set of expressions for which a binding defines a name is called the scope of that name. 

##### Internal definitions and block structure
Localize subprocedures, hiding them inside sqrt. We allow a procedure to have internal definitions that are local to that procedure.


## Procedures and the processes they generate

A procedure is a pattern for the local evolution of a computational process.

### Linear recursion and iteration

Factorial function n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

Compute n! by computing (n-1)!

The expansion builds up a chain of deferred operations and contraction occurs when operations are eperformed. This type of process, characterised by deferred operations, is called a recursive process.

The length of the chain of deferred operation and hence amount of info needed to keep track of it, grows linearly with N. Such a process is linear recursion process.

The fact-iter program does not grow or shrink. It is an iterative process where state can be summarised by a fixed number of state variables.

It is a linear iterative process.

Some languages are designed such that interpretation of any recursive procedure consumes memory that grows with procedure calls, even if the process is iterative.

An implementation that is able to execute an iterate process in constant space is called tail-recursive.

### Tree recursion

Fibonacci numbers is defined by fib(n) = fib(n-1) + fib(n-2) for n >= 2. 

The evovled process looks like a tree. This is because fib procedure calls itself twice each time it is invoked.

The value of fib(n) grows exponentially with n where (goldenratio)**n/sqrt(5)

Number of steps required by a tree recursive process is proportional to the number of nodes. Space required will be the maximum depth of the tree.


### Orders of growth

Obtain a gross measure of the resources required by the process as inputs become larger.


### Exponentiation

Computing exponential of a given number. Take a base b and positive integer exponent n and computes b**n


b**0 = 1
b**n = b * b**(n-1)


### Greatest common divisors

The GCD of two integers (a, b) is largest integer that divides both a and b with no remainder.

If r is the remainder of a/b, then gcd(b, r) == gcd(a, b) so computing a GCD is a problem of computing GCD of smaller numbers

This method is known as Euclid's algorithm.

### Primality test

Two methors to check primality of an integer

#### Searching for divisors

Test if a number is prime by finding divisors. Test if number is divisible by numbers starting with 2

#### Fermat test

Fermat's little theorem: if n is a prime number and a is a positive integer less than n, a raised to nth power is congruent to a modulo n

Two numbers are congruent modulo n if they both have the same remainder when divided by n


The idea of Fermat's test is to test random numbers. If a**n modulo n is not equal to a, then n is not prime.

One approach to coping with redundant computations is to arrange matters so we construct table of values as they are computed. This strategy is known as memoization. 

Elements of Pascal's triangle is called binomial coefficients as nth row consists of coefficients in (x+y)^n

## Formulating abstractions with higher order procedures

Procedures that manipulate procedures are called higher-order procedures.


(define (<name> a b)
    (if (> a b)
        0
        (+ (<term> a)
        (<name> (<next> a) b))))

To compute over a range(a, b), we need a way to accumulate the results and get next number. 

Sum and product are both special cases of a still more generation notion called accumulate that combines a collection of terms.

(accumulate combiner null-value term a next b)

### Constructing procedures using lambda

Seems awkward to define trivial procedures. More convenient to have a way to directly specify procedure that returns its input.

Introduce a special form lambda which creates procedure

(lambda (x) (+ x 4))

(lambda (<formal-parameters>) <body>)

### Using let to create local variables

(let ((a (+1 (* x y))))
      (b (- 1 y)))

(let ((<var1> <exp1>)
      (<var2> <exp2>)
      ...)
      <body>)

Let var1 have value exp1, var2 have value exp2 ... in body

First part of let is a list of name-expression pairs
The body of let is evaluated with these names bound as local variables

Let allows one to bind variables as locally as possible. 
