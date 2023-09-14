#!/usr/bin/env python3
"""Rotates a 2D matrix 90 degrees clockwise."""


import copy


def rotate_2d_matrix(matrix):
    """ Rotates a 2 d matrix"""
    temp = copy.deepcopy(matrix)
    k = 0
    v = 0
    i = -1
    j = 0

    matrix_len = len(matrix)
    matrix_inner_len = len(matrix[0])

    for _ in range(matrix_len):
        for _ in range(matrix_inner_len):
            matrix[k][v] = temp[i][j]
            v = v + 1
            i = i - 1
        k = k + 1
        j = j + 1
        v = 0
        i = -1
