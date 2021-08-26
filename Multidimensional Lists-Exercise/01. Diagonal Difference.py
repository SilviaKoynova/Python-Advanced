n = int(input())
matrix = []
for _ in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

primary_diagonal = 0
secondary_diagonal = 0
for index in range(n):
    primary_diagonal += matrix[index][index]
for i in range(0, n):
    secondary_diagonal += matrix[i][n - i - 1]
difference = abs(primary_diagonal - secondary_diagonal)
print(difference)