import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "02 input.txt")

with open(path, "r") as f:
    data = f.read().split(',')

result = []

for item in data:
    lower, upper = map(int, item.split('-'))

    for value in range(lower, upper+1):
        value_str = str(value)
        value_str_len = len(value_str)

        len_denominators = [i for i in [2, 3, 5] if value_str_len % i == 0]


        if len(set(value_str)) == 1: #denominator=1
            print(f'found incorrect id: {value}')

            result.append(value)
            continue

        if 2 in len_denominators:
            value_str_middle = value_str_len // 2 #denominator=2
            
            value_str_12 = value_str[0:value_str_middle]
            value_str_22 = value_str[value_str_middle:]
            val_set = set([value_str_12, value_str_22])

            
            if len(val_set) == 1:
                print(f'found incorrect id (halves): {value}, x2 of {val_set}')

                result.append(value)
                continue
        
        if 3 in len_denominators:
            value_str_third = value_str_len // 3 #denominator=3
            value_str_13 = value_str[:value_str_third]
            value_str_23 = value_str[value_str_third:value_str_third*2]
            value_str_33 = value_str[value_str_third*2:value_str_third*3]
            
            val_set = set([value_str_13, value_str_23, value_str_33])
            if len(val_set) == 1:

                print(f'found incorrect id (thirds): {value}, x3 of {val_set}')

                result.append(value)
                continue

        if 5 in len_denominators:
            value_str_fifth = value_str_len // 5 #denominator=5
            value_str_15 = value_str[:value_str_fifth]
            value_str_25 = value_str[value_str_fifth*1:value_str_fifth*2]
            value_str_35 = value_str[value_str_fifth*2:value_str_fifth*3]
            value_str_45 = value_str[value_str_fifth*3:value_str_fifth*4]
            value_str_55 = value_str[value_str_fifth*4:]
            
            val_set = set([value_str_15, value_str_25, value_str_35, value_str_45, value_str_55])
            if len(val_set) == 1:

                print(f'found incorrect id (fifths): {value}, x5 of {val_set}')

                result.append(value)
    
# print(result)
print(sum(result))