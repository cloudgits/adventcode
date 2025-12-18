import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "03 input.txt")

with open(path, "r") as f:
    data = [line.strip() for line in f.readlines()]

result = 0

for item in data:
    number_str = ''
    left_border = -len(item)

    while len(number_str) < 12:

        max_digit = ''
        right_border = -11 + len(number_str)

        if right_border == 0:
            right_border = None

        max_digit = max(item[left_border:right_border])
        number_str += max_digit
        slice_index = item[left_border:right_border].index(max_digit)

        if slice_index == 0:
            left_border += 1
        else:
            left_border += 1 + slice_index
       
    result += int(number_str)
    print(f'item_answer: {number_str}')
    
print('result:', result)