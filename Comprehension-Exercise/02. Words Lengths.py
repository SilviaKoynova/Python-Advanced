text = input().split(', ')
print(*[f"{name} -> {len(name)}" for name in text], sep=', ')