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
    >>>



"""
