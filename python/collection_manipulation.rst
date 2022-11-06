Collection Manipulation
=======================

See `datatypes.rst` to get an idea about collections.

List manipulation
-----------------

    assignment:

        Here we are taking an instance of a list.

        >>> my_list = ['foo', 3]
        ... # or my_list = list(('foo', 3))

    indexing:

        We can index only the ordered collection. Unordered collections are not indexable.

        If we want to see an item in a list we can do so by using ZEROth
        (index of the first item is zero) indexing.

        >>> my_list[0]
        'foo'
        >>> my_list[1]
        3

        We can also index an iterable using negative indexing.

        >>> my_list[-1]
        3
        >>> my_list[-2]
        'foo'

        PS> A tuple is also an ordered collection so we can index a tuple the same way.

    Adding an item to a list:

        Add at the end of the list.
        >>> my_list.append('bar')
        >>> my_list
        ['foo', 3, 'bar']

        Add at a known index.
        >>> my_list.insert(1, 'dummy')
        >>> my_list
        ['foo', 'dummy', 3, 'bar']
        >>> my_list.insert(0, True)
        >>> my_list
        [True, 'foo', 'dummy', 3, 'bar']

    Removing an item from a List:

        We can pass the value to remove from a list on the `remove` method of a list.

        >>> my_list.remove('dummy')
        >>> my_list
        [True, 'foo', 3, 'bar']

        We can also remove and get it returned by using the `pop` method of a list.

        >>> my_list.pop(-1)
        'bar'
        >>> some_var = my_list.pop(-1)
        >>> some_var
        3

    Concatenating multiple lists:

        >>> my_second_list = list(('blurry', ))
        >>> my_second_list
        ['blurry']
        >>> final_list = my_second_list + my_list
        ['blurry', True, 'foo']

        Or by using the extend method of a list.

        >>> my_second_list.extend(my_list)
        >>> my_second_list
        ['blurry', True, 'foo']

Dict manipulation
-----------------

    Taking an instance of a dictionary:

        >>> my_dict = {}
        ... # or my_dict = dict()

    Adding an item to a dict:

        >>> my_dict.setdefault('key1', 'valueForK1')
        >>> my_dict.setdefault('key3', False)
        >>> my_dict.get('key1')
        'valueForK1'
        >>> my_dict['key2'] = 1000
        >>> my_dict['key2']
        1000
        >>> my_dict
        {'key1': 'valueForK1', 'key2': 1000, 'key3': False}

    Removing an item from a dictionary:

        >>> del my_dict['key1']
        {'key2': 1000, 'key3': False}
        >>> returned_value = my_dict.pop('key2')
        >>> returned_value
        1000
        >>> my_dict
        {'key3': False}
        >>> my_dict.popitem()
        (`key3`, False)

    Updating a dictionary from another dictionary:

        >>> an_dict = dict(key3=True, key4='BLuh')
        >>> my_dict.update(an_dict)
        >>> my_dict
        {'key3': True, 'key4': 'Bluh'}

Set manipulation
----------------

    Taking an instance of a Set:

        >>> myset = {'foo', 3, 5, 'bar'}
        ... # or set(('foo', 3, 5, 'bar'))

    Adding an item to a set:

        >>> myset.add('dummy')
        >>> myset
        {3, 5, 'bar', 'dummy', 'foo'}

    Removing an item from a set:

        >>> myset.remove('bar')
        >>> myset
        {3, 5, 'dummy', 'foo'}

PS> A tuple object is immutable, so we can not manipulate a tuple after taking
an instance of it.
