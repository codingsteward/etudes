# Introduction to crafting intepreters

Parts of a language/language implementation.

Source code -> scanning -> tokens -> parsing -> syntax tree -> transpiling/analysis/optimising...

Code generation -> bytecode/machine code

## Scanning

First step is scanning or lexing/lexical analysis. A scanner/lexer takes in a linear stream of characters and chunks them into a series of something more akin to words. Each word is caleld a token.

## Parsing

This is where our syntax gets a grammer. Ability of compose larger expressions and statements out of smaller parts.

A parser takes flat sequence of tokens and builds a tree structure that mirrors the nested nature of grammar. It's called parse tree/abstract syntax tree,AST, trees.

Parser's job also reports syntax error.

## Static analysis

Binding/resolution: for each identifier, find out where that name is defined and wire two together.
Scope: region of source code where a certain name can be used to refer to a certain declaration.

If language is statically typed, this is where we type check. If the types don't support operation, we report type error.

We can store these info as attributes on syntax tree itself, or lookup table/symbol table that associates key and identifier to objects.

Most powerful bookkeeping tool is to transform tree into new data structure.

## Intermediate representations

Backend is concerned with final architecture where program will run. In the middle, the code may be stored as IR that is tightly tied to source/destination forms. 

Pascal, C, Fortran => target x87, ARM etc.. can write one frontend for each source language and one backend for each architecture

## Optimization

Swap it out with a different program that has same semantics. One example is constant folding. 

## Code generation

Converting it to a form machine can actually run. Do we generate instructions for real CPU or virtual one? Instead of targeting x86 machine code, we produce virtual machine code. Code for idealized machine or bytecode. 

## Virtual machine

Since no chip speaks that bytecode, translate again. Bytecode is intermediate representation so convert it to run on platform.

## Runtime

If compiled to bytecode, start up VM to run it. Else load executable and off it goes.

We need some services like garbage collector to reclaim unused bits. 

## Tree walk interpreters

Some languages begin executing code right after parsing. It is not widely used as it's slow.

## Transplier

Source to source compiler. Produce a string of valid source code for some other language.

## Just in time compilation
JVM or CLR does this. Compile it to native code for architecture computer supports.

Compiling is an implementation technique that translates source to other forms (bytecode or high level language)

Interpreter means it takes in source code and executes it immediately. It runs programs from source.

