Introducing Python
==================

Python is an interpreted language. A program written in python can only be run
by a python interpreter.

To see if you have the python interpreter installed on your machine try the
following command::

    $ python -V

This command will show an output similar to the following::

    Python 3.8.10

You can also try the following command in the case when the first command does
NOT work::

    $ python3 -V

If you do not have python have python installed you can install python with the
following command::

    $ sudo apt install python3

To launch the python interpreter use one of the following command::

    $ python
    OR
    $ python3

It's a probable case that you might have two different versions of python
installed on your machine. In such a case the command `python` will run a python
version 2 interpreter and the command `python3` will run a python version 3
interpreter. You can see which version of python you are using in the first line
when the python interpreter opens up. An example start-up output of python::

    Python 3.8.10 (default, Nov 26 2021, 20:14:08)
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Here on the last line `>>>` is the actual python prompt, where you can run any
python program.

To exit out from the python interpreter use: `CTRL + D`.

Performing arithmatics in the python interpreter::

    >>> 8 + 8
    16
    >>> 8 / 8
    1.0

The basic task of higher level programming languages involves manipulating some
sort of values. For which we usually have to store the value in something called
`variables`. We can declare a variable following the systax below::

    >>> age_of_sharif = 29

Here `age_of_sharif` is the name of the variable. Such a variable name can only
contain a-z or A-Z or 0-9 or _, anything else on the variable name will make the
name invalid and also a variable name cannot start with a number.

    >>> age_of_sharif
    29
    >>> frist_name = 'Sharif'
    >>> _fristName = 'Sharif'

Errors in programming are widely known as exceptions. An exception name usually
describe in short what was the primary reason of the error. When there's an
exception occured, the program will provide you with a traceback which you can
analyze to discover fixes for the error.

    >>> 0first_name = 'Sharif'
      File "<stdin>", line 1
        0first_name = 'Sharif'
         ^
    SyntaxError: invalid syntax

here, `SyntaxError: invalid syntax` is the exception and::

    File "<stdin>", line 1
      0first_name = 'Sharif'
       ^

the part above is known as the traceback.

    >>> last_name011 = 'Mehedi'

Python built-in types
---------------------

Most common python built-in types that we might encounter are, int, str, float,
list, tuple, dict.

    - int: stands for integer and it is a class of whole number

        Example: 1, 2, 0, -1, 554896645456, and such.

    - float: stands for float and it is a class of fractional number or decimal

        Example: 1.0, 2.5, -6.8, 0.65865 and such.

    - str: stands for string and it is a class of a series of characters inside single quotes (') or double quotes (")

        Example: "tomato", "trees", 'example01@mail.com', "!@#$$%^&ZLKJL", """some str""", '''random channel''' and such.

We would need some ways to manipulate some values of the above types. We can
perform arithmatic operations on `int` and `float` like a regular calculator.

On objects of `str` class we can also perform the plus (+) operation and this
operation is called concatenation (string concatenation).

>>> potato_price_per_kg = 2
>>> quantity_potato_in_kg = 5
>>> total_price = protato_price_per_kg * quantity_potato_in_kg
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'protato_price_per_kg' is not defined

The above exception name is `NameError` and it means the name of a variable is
NOT right. If we look at the traceback it say File "<stdin>", here stdin stands
for standard(std) input(in), basically explains that the line of code that the
program failed to execute came from standard input, and `line 1` means the line
of code it were trying to execute. Even though there are other line of codes
that were above this line, still this line is considered `line 1` because
everything above it has already been executed.

>>> total_price = potato_price_per_kg * quantity_potato_in_kg
>>> total_price
10
>>> float
<class 'float'>
>>> double
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'double' is not defined

There are no built-in type `double` in python.

Looking up the types of objects
-------------------------------

>>> type
<class 'type'>
>>> type(total_price)
<class 'int'>
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
>>> str
<class 'str'>
>>> "some random string"
'some random string'
>>> type("some random string")
<class 'str'>

Manipulating strings (of class str)
-----------------------------------

>>> first_name = "Sharif"
>>> last_name = "Mehedi"

We can use the `+` (plus) operator to concatenate strings.

>>> full_name = first_name + " " + last_name
>>> full_name
'Sharif Mehedi'
>>> first_name + last_name
'SharifMehedi'

There is a built-in *function* `dir` that shows the attributes, properties and
methods of a class.

>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'first_name', 'full_name', 'last_name', 'potato_price_per_kg', 'quantity_potato_in_kg', 'total_price']
>>> dir(first_name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill']

What is a class?

class
-----

A class is something that extends the python types.

A class definition looks like the following::

    color = "green"

    class Food(object):

        color = None
        calories = 0.0
        color_1 = "blue"

    name = "Stupid name"
    color = "red"

In the above example we have defined a class name `Food` that extends the python
type `object` and let's NOT dwell into meaning of what this python type `object`
means for now and let's just take the meaning as the name `object` suggest that
it is simply some generic object.

A class definition must start with the keyword `class`.

If we look at the above example, the line 205 is the line where the definition
of `Food` starts. A definition must start with some keyword, which in this case
is `class` and must end with a colon (:). And to have attributes defined for
this `class`/`Food` we must follow the `rule of indentation`.

The rule of indentation
-----------------------

Everything that belongs to a defined object must have a certain number of
whitespaces before them. We programmer shortly user the `Tab` key in the
keyboard. You can set your choice of indentation on your text editor. I
personally like to have 4 whitespaces is indentation, so I myself set the value
for the `Tab` key to give 4 whitespaces. But you can choose 2 or 1 or 6
basically, maybe the number you like most.


What does attributes, properties and methods mean?

attribute:

  An attribute is a variable defined within the local scope of a class. To say
  in simpler term, let's say an attribute is a variable defined within a class.



>>> first_name
'Sharif'
>>> first_name.lower()
'sharif'
>>> First_name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'First_name' is not defined
>>> first_name.upper()
'SHARIF'
>>> first_name.upper().capitalize()
'Sharif'
>>>
