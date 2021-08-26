import sys

rows, cols = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split()])
max_sum = - sys.maxsize
positions = None
for row in range(rows - 2):
    for col in range(cols - 2):
        a11 = matrix[row][col]
        a12 = matrix[row][col + 1]
        a13 = matrix[row][col + 2]
        a21 = matrix[row + 1][col]
        a22 = matrix[row + 1][col + 1]
        a23 = matrix[row + 1][col + 2]
        a31 = matrix[row + 2][col]
        a32 = matrix[row + 2][col + 1]
        a33 = matrix[row + 2][col + 2]
        current_sum = a11 + a12 + a13 + a21 + a22 + a23 + a31 + a32 + a33
        if current_sum > max_sum:
            max_sum = current_sum
            positions = (row, col)
row, col = positions
print(f"Sum = {max_sum}")
print(matrix[row][col], matrix[row][col + 1], matrix[row][col + 2])
print(matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2])
print(matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2])
