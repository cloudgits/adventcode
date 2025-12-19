import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "04 input.txt")


def nuke_paper_rolls(data):
    data_upd = []
    counter = 0
    for row in range(len(data)):
        data_upd.append([])


        for col in range(len(data[row])):


            cell_value = data[row][col]

            if cell_value in ['.', 'x']:


                data_upd[row].append('.')
                continue
            
            current_cell = (row, col)


            adj_rows = [(row-1 if row >= 1 else None), row, (row+1 if row+1 < len(data) else None)]

            adj_cols = [(col-1 if col > 0 else None), col, (col+1 if col+1 < len(data[row]) else None)]


            adjacent = [[adj_row, adj_col] for adj_row in adj_rows for adj_col in adj_cols
                        if adj_row is not None and adj_col is not None and (adj_row, adj_col) != current_cell
                        and data[adj_row][adj_col] == '@'
                        ]


            if len(adjacent) < 4:

                counter += 1
                data_upd[row].append('x')
            else:

                data_upd[row].append('@')


    return counter, data_upd


with open(path, "r") as f:
    data = [line.strip() for line in f.readlines()]














data = [[c for c in line] for line in data]
for item in data:
    print(*item)
print()










result = 0

while True:
    cells_nuked, data_upd = nuke_paper_rolls(data)
    if cells_nuked == 0:
        print(f'result: {result}')
        break

    print(f'cells nuked: {cells_nuked}')


    data = data_upd
    result += cells_nuked
    
