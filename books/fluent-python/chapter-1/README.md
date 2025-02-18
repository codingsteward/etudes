# Chapter 1: The python data model

The python interpreter invokes special methods to perform basic operations. Special methods are written with leading and trailing double underscores.

obj[key] is supported by __getitem__ special method.

## Pythonic card deck

With just implementing two special methods: __getitem__ and __len__, it automatically supports slicing, class is iterable

- Iteration is implicit. If a collection has no __contains__, in operator does a sequential scan.

- Most of its functionality comes from leverage data model and composition. By implementing the special methods, the card deck behaves like a standard Python sequence and benefit from core language features (e.g. iterations and slicing) and standard library (random.choice, reversed, sorted)

- Card deck cannot be shuffled as it's immutable.

## Emulating enumeric types

Several special methods allow user objects to respond to operators such as +

Vector class to represent two-dimensional vectors. Example usage:
v1 = Vector(2, 4)
v2 = Vector 2, 1)
v1 + v2 == Vector(4, 5)

- __add__ implements + operator
- __mul__ implements * operator which allows Vector * scalar, __rmul__ for other direction
- __repr__ called by repr to get string representation for inspection. !r get the standard representation of attributes to be displayed in f-string. It should be unambiguous.
- __str__ is called by the str() built-in and used by print function. Return a string suitable for display to end users.

## Boolean value of a custom type

To determine if a value is truthy or falsy, Python applies bool(x)

By default, instances of user-defined classes are truthy unless __bool__ or __len__ is implemented. 
- bool(x) calls x.__bool__(). If not implemented, it calls x.__len__() and if it returns 0, it returns False. Otherwise, True

- Vector boolean is False if magnitude is zero

## Chapter summary

By implementing special methods, your objects can behave like built-in types. 
