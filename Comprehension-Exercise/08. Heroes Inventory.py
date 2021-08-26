heroes = input().split(', ')
data = input()
inventory = {hero: {} for hero in heroes}
while not data == 'End':
    hero, item_name, item_cost = data.split('-')
    if item_name not in inventory[hero]:
        inventory[hero][item_name] = int(item_cost)
    data = input()
for hero in heroes:
    cost = sum(inventory[hero].values())
    item_count = len(inventory[hero])
    print(f"{hero} -> Items: {item_count}, Cost: {cost}")
