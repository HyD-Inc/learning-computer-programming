
The most basic build in data types in python
============================================

Data in urls:

    https://google.com/?query=buy+books&author=carlos+ruiz+zafon&price_max=500&duh&foo&bar

Here everything that comes after the "?" mark needs to be parsed by the server. The
server would parse it into different data types.

- int

    The int type in python is a 64-bit whole number.

    >>> '0b1111111111111111111111111111111111111111111111111111111111111111'
    ... # This is the biggest possible integer in python but shown in base 2

    Convertion of the binary

        2^63 * 1 + 2^62 * 1 + ... + 2^1 * 1 + 2^0 * 1

    >>> 64
    >>> -60

- float

    The float type in python is a decimal number.
    The first bit of a float indicates the sign (either +ve or -ve)
    The next eleven bits indicates the exponent of the number.
    And the remaining bits are the numbers after the decimal.

    >>> 19.48556
    >>> -54.45684

- string

    String type is a sequence of characters wrapped within inverted commas.

    >>> "This is an example string"
    >>> 'Other dummy string'
    >>> """This
    ... can be
    ... a paragraph."""

- Boolean

    Boolean is either True or False

- None

    Used to indicate nothing for a value.

Categorization of some data types
---------------------------------

- Mutable types

    A mutable is something that can be changed in place.

        - List

            A list is an array of other data types.

            From the url, when a parser parse it will convert "&duh&foo&bar"
            into a list.

            >>> # After the parser
            ... ['duh', 'foo', 'bar']

            A list is an ordered collection.

        - Dict

            A dictionary contains key, value pairs, of any data types.

            From the url, a parser would convert
            "query=buy+books&author=carlos+ruiz+zafon&price_max=500"
            into a dictionary of the form.

            >>> # After the parser
            ... {
            ...     'query': 'buy books',
            ...     'author': 'carlos ruiz zafon',
            ...     'price_max': 500
            ... }

            A dict is an unordered collection.

        - Set

            A set is a collection of unique values of any data type.

            >>> {'ball', 'bat', 'stamps'}

            A set is an unordered collection.

- Immutable types

    An immutable is something that can not be changed in place.

        - Tuple

            A tuple is a collection of values of any data types.

            >>> ('foo', 'dummy', 10, 9.5)

            A tuple is an ordered collection.

- Ordered collection

    Data values are gathered in a sequential order.

- Unordered collection

    There are no meaningful order in a collection of this type.
