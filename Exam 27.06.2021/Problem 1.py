from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk = deque([int(m) for m in input().split(", ")])
milkshakes = 0
ready = False

while chocolates and milk:
    current_chocolate = chocolates.pop()
    current_milk = milk.popleft()
    if current_chocolate <= 0:
        if current_milk > 0:
            milk.appendleft(current_milk)
        continue
    if current_milk <= 0:
        if current_chocolate > 0:
            chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        milk.append(current_milk)
        current_chocolate -= 5
        if not current_chocolate <= 0:
            chocolates.append(current_chocolate)

    if milkshakes == 5:
        ready = True
        break
if ready:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(choko) for choko in chocolates])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(cup) for cup in milk])}")
else:
    print("Milk: empty")