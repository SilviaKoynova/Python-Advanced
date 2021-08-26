from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = list(map(int, input().split()))
intelligence_value = int(input())
locks = deque(locks)
shot_bullets = 0
total_bullets_shot = 0
while bullets:
    if len(locks) == 0:
        break
    current_lock = locks[0]
    current_bullet = bullets.pop()
    if current_bullet <= current_lock:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')
    shot_bullets += 1
    total_bullets_shot += 1
    if shot_bullets == barrel_size and len(bullets) != 0:
        print('Reloading!')
        shot_bullets = 0
if len(bullets) == 0 and len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
elif len(locks) == 0:
    bullet_cost = total_bullets_shot * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - bullet_cost}")
