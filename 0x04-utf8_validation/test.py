#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data1 = [65]
print(validUTF8(data1))  # Output: True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Output: True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # Output: False

data4 = [194, 162, 195, 169, 226, 130, 172]
print(validUTF8(data4))  # Output: True

data5 = [197, 130, 197, 164, 197, 164]
print(validUTF8(data5))  # Output: True

data6 = [0xC0, 0x80]
print(validUTF8(data6))  # Output: False

data7 = [0xE2, 0x82, 0xAC, 0xF0, 0xA4, 0xAD, 0xA2]
print(validUTF8(data7))  # Output: True

data8 = [240, 157, 142, 128]
print(validUTF8(data8))  # Output: True

data9 = [0xED, 0x9F, 0xBF]
print(validUTF8(data9))  # Output: False
