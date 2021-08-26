categories = {category: [] for category in input().split(", ")}
n = int(input())

quantity = 0
quality = 0

for _ in range(n):
    category, item_name, item_params = input().split(" - ")
    categories[category].append(item_name)

    information_data = item_params.split(";")
    quantity += int(information_data[0].split(":")[1])
    quality += int(information_data[1].split(":")[1])

print(f"Count of items: {quantity}")
print(f"Average quality: {quality/len(categories):.2f}")
[print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]