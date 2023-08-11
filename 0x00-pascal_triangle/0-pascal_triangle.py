#!/usr/bin/python3
""" This module contains the pascal triangle module"""


def pascal_triangle(n):
    """ Args:
    n: the number of lists in our triangle
    Return:
    a lists of lists which has the pascals triangle
    """
    pas = []
    if n <= 0:
        return pas
    else:
        pas.append([1])
        if n > 1:
            for x in range(1, n):
                current = []
                a = 0
                b = 0
                for i in range(0, x+1):
                    try:
                        first_element_above = pas[x-1][a]
                    except IndexError:
                        first_element_above = 0
                    if (b-1 > -1):
                        second_element_above = pas[x-1][b-1]
                    else:
                        second_element_above = 0
                    current.append(first_element_above + second_element_above)
                    a = a + 1
                    b = b + 1
                pas.append(current)

    return pas
