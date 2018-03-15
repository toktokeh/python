# Python #

[Variables](#test)

[Comments](#test)

[Numbers](#test)

[Strings](#test)

[Lists](#test)

[Tuples](#test)

[Dictionaries](#test)

[Sets](#test)

[Comprehensions](#test)

[Flow control](#test)

[Input and output](#test)

[Operators](#test)

[Functions](#test)

[Iterators](#test)

[Generators](#test)

[Decorators](#test)

[Errors and exceptions](#test)

[Modules](#test)

[Packages](#test)

[Python Standard Library](#test)

[Classes](#test)

[Files](#test)

[Regular Expressions](#test)

[Testing](#test)

[Miscellaneous](#test)


## Variables ##

## Comments ##

## Numbers ##

- Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored.

## Strings ##

- Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

```python
>>> word[0] = 'J'
TypeError: 'str' object does not support item assignment
```

- Strings can be concatenated (glued together) with the + operator, and repeated with \*:

```python
>>> 3 * 'un' + 'ium'
'unununium'
```

- Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

```python
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```

## Lists ##

- Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content
- When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function:

```python
for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
```

- To loop over two or more sequences at the same time, the entries can be paired with the zip() function:

```python
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
          print('What is your {0}?  It is {1}.'.format(q, a))
```

```text
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

## Tuples ##

- Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored.

- Unlike lists that are meant to hold homogenous items (items of same type), tuples are the recommended way for working with items of different types.

- Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses).

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
```

- A tuple consists of a number of values separated by commas, for instance:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
```

- The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple.

## Dictionaries ##

- Dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.
- It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary).

- A pair of braces creates an empty dictionary: {}.

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> list(tel.keys())
['irv', 'guido', 'jack']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

- Dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

- Looping through dictionaries

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
        print(k, v)
```

## Sets ##

- A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
- List and dictionary items are mutable. Tuple and set items are immutable.
- List and tuple items may be accessed by index. Dictionary items are accessed by key. Set items cannot be accessed by index.
- Lists and tuples maintain order. Dictionaries and sets are unordered.
- Lists and tuples allow duplication. Dictionary and set items are unique.
- Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary which is a different data structure.

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

---------------------------------

```python
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
print("Numbers:", numbers)
print("Even:", even)
print("Odd:", odd)
print("1 in numbers:", 1 in numbers)
print("even.issubset(numbers):", even.issubset(numbers))
print("numbers.issuperset(odd):", numbers.issuperset(odd))
print("even | odd:", even | odd)
print("even & odd:", even & odd)
print("numbers - even:", numbers - even)
```

```text
Output:
Numbers: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Even: {8, 10, 2, 4, 6}
Odd: {9, 1, 3, 5, 7}
1 in numbers: True
even.issubset(numbers): True
numbers.issuperset(odd): True
even | odd: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even & odd: set()
numbers - even: {1, 9, 3, 5, 7}
```

- Similarly to list comprehensions, set comprehensions are also supported:

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

- Sets are mutable. Frozensets on the other hand, are like sets except that they cannot be changed, i.e. they are immutable:

```python
>>> cities = frozenset(["Frankfurt", "Basel","Freiburg"])
>>> cities.add("Strasbourg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
```

## Comprehensions ##

### List comprehension ###

```python
[x**2 for x in range(10)]
```

```python
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

```text
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

- Flatten a list using a listcomp with two 'for'

```python
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- Transpose rows and columns:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

## Flow control ##

## Input and output ##

### Output ###

If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

### String formatting ###

- 3 methods:

```python
age = 24
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))  // recommended
print("My age is %d years" % age)   // deprecated in python 3
```

- To specify width and right-align:

```python
for i in range(1, 12):
    print("{0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))
```

- To specify width and left-align:

```python
for i in range(1, 12):
    print("{0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
```

- To specify precision:

```python
>>> from math import pi  # pi ~ 3.141592653589793
>>> '{0:.2f}'.format(pi)
'3.14
```

### Literal String Interpolation (Python 3.6) ###

## Operators ##

## Functions ##

## Iterators ##

## Generators ##

## Decorators ##

## Errors and exceptions ##

## Modules ##

## Packages ##

## Python Standard Library ##

## Classes ##

## Files ##

## Regular Expressions ##

## Testing ##

## Miscellaneous ##

- Lambda Operator, Filter, Reduce and Map

- Lambda expressions (sometimes called lambda forms) are used to create anonymous functions.

- lambda_expr        ::=  "lambda" [parameter_list]: expression

- Object Oriented Programming / Classes / Class and Instance Attributes / Properties vs. getters and setters

- Inheritance / Multiple Inheritance

- Magic Methods and Operator Overloading

- Meta classes

- Abstract Classes
