from collections import deque

cups_capacity = list(map(int, input().split()))
bottles_with_watter = list(map(int, input().split()))
cups = deque(cups_capacity)
wasted_water = 0
while cups and bottles_with_watter:
    current_cup = cups[0]
    current_bottle = bottles_with_watter[-1]
    if current_cup > current_bottle:
        reduced_value = current_cup - current_bottle
        current_bottle = bottles_with_watter.pop()
        while reduced_value > 0 and bottles_with_watter:
            next_bottle = bottles_with_watter[-1]
            if next_bottle > reduced_value:
                wasted_water += (next_bottle - reduced_value)
                reduced_value -= next_bottle
            else:
                reduced_value -= next_bottle
            bottles_with_watter.pop()
        cups.popleft()
    else:
        wasted_water += current_bottle - current_cup
        bottles_with_watter.pop()
        cups.popleft()
if bottles_with_watter:
    print(f"Bottles: {' '.join(map(str, bottles_with_watter))}")
elif cups:
    print(f"Cups: {' '.join(map(str, cups))}")
print(f"Wasted litters of water: {wasted_water}")
