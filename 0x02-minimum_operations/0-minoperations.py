#!/usr/bin/python3
""" This module contains the minimum operations function"""


def minOperations(n):
    """ Calculates the least number of operations needed to achiev n 'H' characters

    Args: 
    n (int): the number passed 
    Returns:
    int: least number of operations
    """
    number = n
    operations = 0
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            operations = operations + divisor
            number = number / divisor
        else:
            divisor = divisor + 1
            
    return operations
