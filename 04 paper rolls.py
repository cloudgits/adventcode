import os

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, "04 input.txt")

with open(path, "r") as f:
    data = [line.strip() for line in f.readlines()]

counter = 0

for row in range(len(data)):

    for col in range(len(data[row])):
        cell_value = data[row][col]

        if cell_value == '.':
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

print(counter)