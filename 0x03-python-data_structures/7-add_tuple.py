#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    list1 = tuple_a + ('0', '0')
    list2 = tuple_b + ('0', '0')

    var1 = int(list1[0]) + int(list2[0])
    var2 = int(list1[1]) + int(list2[1])

    return (var1), (var2)
