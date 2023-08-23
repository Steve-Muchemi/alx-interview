#!/usr/bin/python3
"""
A method that determins if a given data set
represents a valid UTF8-encoding
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Returns true ifdata is valid UTF-8 encoding
    Args: data - the list of ints to check
    """
    points = 0
    bi = []

    for byte in data:
        bi.append(byte & 0xFF)

    for byte in bi:

        if points == 0:
            if byte >> 3 == 0b11110:
                points = 3

            elif byte >> 4 == 0b1110:
                points = 2

            elif byte >> 5 == 0b110:
                points = 1

            elif byte >> 7 == 0:
                points = 0

            else:

                return False
        else:

            if byte >> 6 != 0b10:
                return False
            points = points - 1

    return points == 0
