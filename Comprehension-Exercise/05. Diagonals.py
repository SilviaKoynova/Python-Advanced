n = int(input())
matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][n - i - 1] for i in range(n)]
print(f"First diagonal: {', '.join([str(num) for num in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f'Second diagonal: {", ".join([str(num) for num in second_diagonal])}. Sum: {sum(second_diagonal)}')