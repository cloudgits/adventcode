import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "02 input.txt")

with open(path, "r") as f:
    data = f.read().split(',')

result = 0

for item in data:
    lower, upper = map(int, item.split('-'))

    for value in range(lower, upper+1):
        value_str = str(value)
        value_str_len = len(value_str)
        value_len_is_even = value_str_len % 2 == 0

        if not value_len_is_even:
            continue
        else:
            value_str_middle = value_str_len // 2
            value_str_left = value_str[0:value_str_middle]
            value_str_right = value_str[value_str_middle:]
            
            if value_str_left == value_str_right:
                print(f'found incorrect id halves: {value}')
                result += value

print(result)