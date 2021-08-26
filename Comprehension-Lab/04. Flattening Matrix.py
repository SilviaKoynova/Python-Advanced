# n = int(input())
# nums = []
# for _ in range(n):
#     nums.extend(input().split(', '))
#
# print([int(el) for el in nums])
n = int(input())
matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
flat_nums = [num for sublist in matrix for num in sublist]
print(flat_nums)
