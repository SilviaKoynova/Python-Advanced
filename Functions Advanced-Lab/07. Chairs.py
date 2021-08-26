# from itertools import combinations
#
# result = list(combinations(input().split(', '), float(input())))
# for x, y in result:
#     print(x, y, sep=', ')


from itertools import combinations

names = input().split(", ")
n = int(input())

print(*[f"{', '.join(el)}" for el in list(combinations(names, n))], sep='\n')


