Control flow and loop
=====================

if, elif, else statements

We will see how we can control the flow of an algorithm using the above
mentioned statements. We will use comparison and logical operators along
with the above keywords:

    - Anatomy

        >>> if condition:
        ...     statement

        >>> if condition:
        ...     statement
        ... elif another_condition:
        ...     statement
        ... else:
        ...     statement

    - Examples

    >>> name = 'dummy'
    >>> if name == 'dummy':
    ...     print(name)
    'dummy'
    >>> num = 10
    >>> if num > 5:
    ...     print(num)
    ... else:
    ...     print('Executing else statement!')
    10
    >>> l_name = len(name)
    >>> l_name
    5
    >>> if num > l_name:
    ...     print(num)
    ... elif num < l_name:
    ...     print("num less then l_name")
    ... else:
    ...     print('Executing else statement!')
    10

Switch in python
----------------

We use `match` and `case` keywords to emulate some switches in python

    - Anatomy

    >>> match condition:
    ...     case match_case1:
    ...         statement
    ...     case match_case2:
    ...         statement
    ...     ...

    - Examples

    >>> match num:
    ...     case 9:
    ...         print(9)
    ...     case 10:
    ...         print(10)
    ...     case 11:
    ...         print(11)
    10

Loops
-----

while loop
----------

    - Anatomy

        >>> while condition:
        ...     statement

    Such loops continues to execute as long as the `condition` is valid.

    - Examples

        >>> while num > 0:
        ...     print(num)
        ...     num -= 1
        10
        9
        8
        7
        6
        5
        4
        3
        2
        1

        >>> while num >= 0:
        ...     num += 1
        ...     print(num)
        ...     if num == 6:
        ...         break
        1
        2
        3
        4
        5
        6

for loop
--------

    - Anatomy

        >>> for item in Iterable|Generator:
        ...     statement

    The `range` function:

        We can use the range in three different ways;

        - one argument

            if only one argument is given range generates integers from
            0 to the (argument_given - 1)

        - two arguments

            if two arguments are given, range generates integers from
            argument_one to (argument_two - 1)

        - three arguments

            if three arguments are given, range generates integers from
            argument_one to (argument_two - 1)
            in steps of (equal to) argument_three

    - Examples:

        >>> for num in range(10):
        ...     print(num)
        ...
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9

        >>> for num in range(1, 11):
        ...     print(num)
        ...
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10

        >>> for num in range(1, 10, 3):
        ...     print(num)
        ...
        1
        4
        7

        >>> list_name = ['alex', 'rubayet', 'naser']
        >>> for name in list_name:
        ...     print(name)
        alex
        rubayet
        naser
