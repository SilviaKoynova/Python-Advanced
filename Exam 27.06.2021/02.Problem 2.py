def validator(ro, co, size):
    if 0 <= ro < size and 0 <= co < size:
        return True
    return False


matrix = []
player = []
counter = 0
for row_index in range(5):
    current_row = input().split()
    if 'A' in current_row:
        player = [row_index, current_row.index('A')]
    counter += current_row.count('x')
    matrix.append(current_row)
targets_left = counter
row = player[0]
col = player[1]
win = False
positions = []
number_of_commands = int(input())
while True:
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == 'move':
        steps = int(command[2])
        if direction == 'up':
            r = row - steps
            c = col
            if validator(r, c, 5):
                if matrix[r][c] == '.':
                    matrix[r][c] = 'A'
                    matrix[row][col] = '.'
                    row, col = r, c
        elif direction == 'down':
            r = row + steps
            c = col
            if validator(r, c, 5):
                if matrix[r][c] == '.':
                    matrix[r][c] = 'A'
                    matrix[row][col] = '.'
                    row, col = r, c
        elif direction == 'left':
            r = row
            c = col - steps
            if validator(r, c, 5):
                if matrix[r][c] == '.':
                    matrix[r][c] = 'A'
                    matrix[row][col] = '.'
                    row, col = r, c
        elif direction == 'right':
            r = row
            c = col + steps
            if validator(r, c, 5):
                if matrix[r][c] == '.':
                    matrix[r][c] = 'A'
                    matrix[row][col] = '.'
                    row, col = r, c
    elif action == 'shoot':
        targets = 0
        if direction == 'up':
            r = row - 1
            c = col
            while validator(r, c, 5):
                if matrix[r][col] == 'x':
                    targets += 1
                    targets_left -= 1
                    positions.append([r, c])
                    break
                else:
                    r = r - 1
                    c = c
        elif direction == 'down':
            r = row + 1
            c = col
            while validator(r, c, 5):
                if matrix[r][c] == 'x':
                    targets += 1
                    targets_left -= 1
                    matrix[r][c] = '.'
                    positions.append([r, c])
                    break
                else:
                    r = r + 1
                    c = c
        elif direction == 'left':
            r = row
            c = col - 1
            while validator(r, c, 5):
                if matrix[r][c] == 'x':
                    targets += 1
                    targets_left -= 1
                    matrix[r][c] = '.'
                    positions.append([r, c])
                    break
                else:
                    r = r
                    c = c - 1
        elif direction == 'right':
            r = row
            c = col + 1
            while validator(r, c, 5):
                if matrix[r][c] == 'x':
                    targets += 1
                    targets_left -= 1
                    matrix[r][c] = '.'
                    positions.append([r, c])
                    break
                else:
                    r = r
                    c = c + 1
        if targets_left == 0:
            print(f"Training completed! All {counter} targets hit.")
            win = True
            break
    number_of_commands -= 1
    if number_of_commands == 0:
        break


if not win:
    print(f"Training not completed! {targets_left} targets left.")
for p in positions:
    print(p)






