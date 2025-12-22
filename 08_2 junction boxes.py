import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "08 input.txt")

with open(path, "r") as f:
    junc_coords = [tuple([int(i) for i in line.strip().split(',')]) for line in f.readlines()]
    


def get_point_distances(xyz_coords):

    result = []
    
    for i in range(len(xyz_coords)):
        for j in range(i+1, len(xyz_coords)):
            point1 = xyz_coords[i]
            point2 = xyz_coords[j]
            x1, y1, z1 = point1
            x2, y2, z2 = point2
            distance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** 0.5

            result.append((distance, point1, point2))

    result = sorted(result)

    return result


p_distances =  get_point_distances(junc_coords)

chains = {}
chain_number = 0

for pair in p_distances:

    distance, p1, p2 = pair
    p1_chain = None
    p2_chain = None

    for key in chains:
        if p1 in chains[key]:
            p1_chain = key
        if p2 in chains[key]:
            p2_chain = key

    if p1_chain is None and p2_chain is None:
        chains[chain_number] = [p1, p2]
        chain_number += 1

    elif p1_chain is not None and p2_chain is None:
        chains[p1_chain].append(p2)

    elif p2_chain is not None and p1_chain is None:
        chains[p2_chain].append(p1)

    elif p1_chain is not None and p2_chain is not None:

        if p1_chain == p2_chain:
            continue
        else:
            chains[p1_chain].extend(chains[p2_chain])
            chains.pop(p2_chain, None)
    if len(chains) == 1:
        print(p1, p2)

count = 0
answer = 1


for key in sorted(chains, key=lambda k: len(chains[k]),reverse=True):
    chain_length = len(chains[key])
    
    print(f"c{count}: {chain_length}")
    answer *= chain_length

    count += 1
    if count == 3:
        print(f'answer: {answer}')
        break