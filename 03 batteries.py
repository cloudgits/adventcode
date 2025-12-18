import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "03 input.txt")

with open(path, "r") as f:
    data = [line.strip() for line in f.readlines()]

# data = ['987654321111111',
#         '811111111111119',
#         '234234234234278',
#         '818181911112111']

result = 0

for item in data:
    max_first = max(item[:-1])
    max_first_index = item.index(max_first)

    max_last = max(item[max_first_index+1:])

    print(f'{max_first}{max_last}')

    number = int(max_first+max_last)
    result += number

print(result)