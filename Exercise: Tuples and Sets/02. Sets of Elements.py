n, m = input().split()
n = int(n)
m = int(m)
first = set()
second = set()
for _ in range(n):
    first.add(input())
for _ in range(m):
    second.add(input())
common = first.intersection(second)
[print(el) for el in common]
