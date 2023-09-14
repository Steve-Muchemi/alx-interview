#!/usr/bin/env python3

original_matrix= [[1,2,3],[4,5,6],[7,8,9]]

num_rows = len(original_matrix)
num_cols = len(original_matrix[0])
new_matrix = []

for i in range(num_rows):
    row = []
    for j in range(num_cols):
        row.append(original_matrix[j])
    new_matrix.append(row)

for row in new_matrix:
    print(row)
