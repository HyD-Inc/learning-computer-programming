Operators in python
===================

The arithmatic operators in python
----------------------------------

(+, -, *, /, //, %)

    + (plus) operator

        Used for adding two numbers and concatenating objects.

        >>> 4+6
        10

    - (minus OR high-pen) operator

        Used for subtracting two numbers.

        >>> 6-4
        2

    * (asterisk OR multiply) operator

        Used for multiplying two numbers.

        >>> 4 * 2
        8

    ** (double asterisk OR power OR exponent) operator

        Take order of exponent of the second number on the first number.

        >>> 4 ** 2
        16

    / (back-slash OR division) operator

        Used for dividing two numbers. The result of a division is always a float.

        >>> 9 / 3
        3.0

    // (double back-slash OR floor division) operator

        Used for dividing two numbers. The result of a division is always an integer
        taking the "lower bound" of the result (hence floor (division)).

        >>> 23 // 8
        2

    % (percent OR modulo) operator

        Used for taking the remainder (of an assumed floor division).

        >>> 23 % 8
        7

The assignment operators in python
----------------------------------

    = (equal) operator

        Used to store some values in some named variable.

        >>> my_int = 9
        >>> my_int
        9

    += (plus equal) operator

        >>> my_int += 4
        ... # this is a shortcut for my_int = my_int + 4
        >>> my_int
        13

    -= (minus equal) operator

        >>> my_int -= 2
        ... # this is a shortcut for my_int = my_int - 2
        >>> my_int
        11

    *= (multiply equal) operator

        >>> my_int *= 2
        >>> my_int
        22

    /= (division equal) operator

        >>> my_int /= 2
        >>> my_int
        11

    //= (floor division equal) operator

        >>> my_int //= 2
        >>> my_int
        5

    **= (power equal) operator

        >>> my_int **= 2
        >>> my_int
        25

    %= (modulo equal) operator

        >>> my_int %= 2
        >>> my_int
        1

The comparison operators in python
----------------------------------

    == (double equal) operator

        Tests if the values are same.

            >>> my_int == 1
            True
            >>> my_int == "a"
            False

    > (grater then) operator

        >>> my_int > 0
        True
        >>> my_int > 8
        False

    < (less then) operator

        >>> my_int < 0
        False
        >>> my_int < 8
        True
        >>> my_int < 1
        False

    >= (grater equal) operator

        >>> my_int >= 1
        True
        >>> my_int >= 0
        True
        >>> my_int >= 5
        False

    <= (less equal) operator

        >>> my_int <= 1
        True
        >>> my_int <= 0
        False
        >>> my_int <= 5
        True

    != (not equal) operator

        >>> my_int != 1
        False
        >>> my_int != 0
        True

The logical operators in python
-------------------------------

    "and" operator

        Both the objects around the "and" operator must be of
        boolean "True" for the result to be "True".

        >>> True and True
        True
        >>> True and False
        False
        >>> 1 and True
        True
        >>> 0 and True
        False

    "or" operator

        Only one the objects around the "and" operator must be of
        boolean "True" for the result to be "True".

        >>> True or True
        True
        >>> True or False
        True
        >>> 1 or True
        True
        >>> 0 or True
        True
        >>> False or False
        False
        >>> 0 or False
        False

The identity operator in python
-------------------------------

    "is" operator

        Both the objects around the "is" operator must be the same
        object for the result to be "True"

        >>> 1 is True
        False
        >>> my_int is 1
        True

    "is not" operator

        Only negates the "is" operator.

        >>> 1 is not False
        True
        >>> my_int is not 1
        False
