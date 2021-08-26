from collections import deque

total_food_quantity = int(input())
orders = deque(list(map(int, input().split())))
print(max(orders))
while orders:
    current_order = orders.popleft()
    if total_food_quantity >= current_order:
        total_food_quantity -= current_order
    else:
        orders.appendleft(current_order)
        print(f"Orders left: {' '.join(str(i) for i in list(orders))}")
        break
if not orders:
    print("Orders complete")