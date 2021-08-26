n = int(input())
table = set()
for _ in range(n):
    elements = input().split()
    for el in elements:
        table.add(el)
[print(e) for e in table]