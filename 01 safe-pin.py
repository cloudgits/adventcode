import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "01 input.txt")

with open(path, "r") as f:
    data = f.readlines()


act_pos = 50
stopped_at_zero = 0
crossed_zero = 0
full_rotations = 0


print(f'the dial is at:{act_pos}')

for item in data:

    direction = item[0]
    delta = int(item[1:]) if direction == 'L' else -int(item[1:])

    full_rotations += abs(delta) // 100

    remainder = abs(delta) % 100
    if delta < 0:
        remainder = -remainder
    
    new_pos = act_pos + remainder
    print(f'pos:{act_pos} delta:{delta} new_pos:{new_pos}')

    if new_pos > 100:
        crossed_zero += 1
        print(f'new pos > 100, zero crossed, adding 1 to crossed_zero')
    elif act_pos > 0 and new_pos < 0:
        crossed_zero += 1
        print(f'new pos < 0, zero crossed, adding 1 to crossed_zero')

    if new_pos % 100 == 0:
        stopped_at_zero += 1
        print(f'stopped at zero! adding +1 to stopped_at_zero')


    act_pos = new_pos % 100

    print()
print(f'stopped at zero:{stopped_at_zero}, crossed zero:{crossed_zero}, full rotations:{full_rotations}')
print(stopped_at_zero + crossed_zero + full_rotations)