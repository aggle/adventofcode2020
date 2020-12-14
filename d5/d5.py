"""
Day 5

Seats are specified using binary space partitioning
"""

input = "./input"

nrow_regions = 7
nrows = 2**nrow_regions
ncol_regions = 3
ncols = 2**ncol_regions

test_data = (
    {'seat': 'FBFBBFFRLR', 'row':  44, 'col': 5, 'seat_id': 357},
    {'seat': 'BFFFBBFRRR', 'row':  70, 'col': 7, 'seat_id': 567},
    {'seat': 'FFFBBBFRRR', 'row':  14, 'col': 7, 'seat_id': 820,},
    {'seat': 'BBFFBBFRLL', 'row': 102, 'col': 4, 'seat_id': 820}
)

# use this to determine the exponent
exponent_map = {'F': 0, 'B': 1, 'L': 0, 'R': 1}

def calc_row_num(seat):
    row_str = list(seat[:7])
    row_vals = [str(exponent_map[i]) for i in row_str]
    row_num = int(''.join(row_vals), base=2)
    return row_num

def calc_col_num(seat):
    col_str = list(seat[7:].strip())
    col_vals = [str(exponent_map[i]) for i in col_str]
    col_num = int(''.join(col_vals), base=2)
    return col_num

def calc_seat_id(seat):
    row_num = calc_row_num(seat)
    col_num = calc_col_num(seat)
    seat_id = row_num * ncols + col_num
    return seat_id


if __name__ == "__main__":
    seat_ids = []
    with open(input, mode='r') as file:
        seat = file.readline()
        while seat != '':
            seat_ids.append(calc_seat_id(seat))
            seat = file.readline()
    print(max(seat_ids))
