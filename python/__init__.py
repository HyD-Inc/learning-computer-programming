"""
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

    >>> 0first_name = 'Sharif'
      File "<stdin>", line 1
        0first_name = 'Sharif'
         ^
    SyntaxError: invalid syntax



    >>> last_name011 = 'Mehedi'

Python built-in types
---------------------

Most common python built-in types that we might encounter are, int, str, float,
list, tuple, dict.

    - int: stands for integer and it is a class of whole number

        Example: 1, 2, 0, -1, and such.

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
>>> total_price = potato_price_per_kg * quantity_potato_in_kg
>>> total_price
10
>>> float
<class 'float'>
>>> double
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'double' is not defined
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
>>> first_name = "Sharif"
>>> last_name = "Mehedi"
>>> full_name = first_name + " " + last_name
>>> full_name
'Sharif Mehedi'
>>> first_name + last_name
'SharifMehedi'
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'first_name', 'full_name', 'last_name', 'potato_price_per_kg', 'quantity_potato_in_kg', 'total_price']
>>> dir(first_name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
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


"""
