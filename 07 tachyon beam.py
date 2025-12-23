import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "07 input.txt")

with open(path, "r") as f:
    data = [line.strip() for line in f.readlines()]


# for line in data:
#     print(line)
# print()
# print()


beam = []
answer = 0

for line in data:
    read = True
    beam = list(set(beam))

    for i in range(len(line)):
        char = line[i]

        if char == 'S':
            beam.append(i)
            read = False
            continue
        
        elif char == '^':
            read = False
            if i in beam:
                answer += 1
                beam.remove(i)
                beam.append(i-1)
                beam.append(i+1)

    if read is False:
        print(sorted(set(beam)))
    
print(answer)