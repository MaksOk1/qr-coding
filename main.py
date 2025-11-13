import sys
sys.dont_write_bytecode = True
# size = 21
# matrix = (
#     [[None for _ in range(size)] for _ in range(size)]
# )

'''
Now using: (NONE | TRUE) scheme
Maybe should switch to (FALSE | TRUE)
Or (0 | 1) scheme
'''


def create_size_by_version(version: int = 1):
    start = 17
    size = start + 4 * version
    print(f"Setted size is - {size}, for qr version - {version}")
    return size

def create_matrix_by_size(size):
    matrix = (
        [[None for _ in range(size)] for _ in range(size)]
    )
    print(f"Created matrix:\n{matrix}")
    return matrix

def get_centre_by_size(size: int):
    centre_cube = int((size - 1) / 2)
    print(f"Centre cube is - {centre_cube}")
    return centre_cube

def set_margins(matrix: list, margin_size: int):
    rows = len(matrix)
    cols = len(matrix[0])
    new_rows = 2 * margin_size + rows
    new_cols = 2 * margin_size + cols

    matrix_with_margin = [[None] * new_cols for _ in range(new_rows)]

    for i in range(rows):
        for j in range(cols):
            matrix_with_margin[i + margin_size][j + margin_size] = matrix[i][j]
    
    return matrix_with_margin








def print_matrix(matrix):
    # _matrix[10][10] = True
    # for row in matrix:
    #     print("".join(("  " if cell != None else "██") for cell in row))
    for row in matrix:
        str = ""
        for cell in row:
            if cell != None and cell != False and cell != 0:
                itr = "  "
            else:
                itr = "██"
        # itr = ("  ")
            str += itr
        print(str)
    print("Matrix displayed")
    # print(f"Current matrix:\n{matrix}")

def make_changes(matrix: list, size: int):
    # set_skyland_cubes(matrix=matrix, size=size)
    # set_finder(matrix=matrix, pos=(0, 0))
    # set_finder(matrix=matrix, pos=(size - 7, 0))
    set_finders(matrix=matrix, size=size)
    return matrix


def set_centre_cube(matrix: list, centre_cube):
    matrix[centre_cube][centre_cube] = True
    print(f"Made change to matrix[{centre_cube}][{centre_cube}]")
    return matrix

def set_finder(matrix: list, pos: tuple):
    start_x, start_y = pos

    pattern = [
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1],
    ]
    
    pattern_size = len(pattern) # pattern width and height are optional
    canvas_size = len(matrix)   # and here too



    for y in range(pattern_size):
        for x in range(pattern_size):
            canvas_x = start_x + x
            canvas_y = start_y + y

            if 0 <= canvas_x < canvas_size and 0 <= canvas_y < canvas_size:
                matrix[canvas_y][canvas_x] = bool(pattern[y][x])
            else:
                pass
    
    return matrix

def set_finders(matrix: list, size: int):
    x_top_left = 0
    y_top_left = 0
    x_top_right = size - 7
    y_top_right = 0
    x_bottom_left = 0
    y_bottom_left = size - 7
    pos_top_left = (x_top_left, y_top_left)
    pos_top_right = (x_top_right, y_top_right)
    pos_bottom_left = (x_bottom_left, y_bottom_left)
    finders = (pos_top_left, pos_top_right, pos_bottom_left)
    for finder_pos in finders:
        set_finder(matrix=matrix, pos=finder_pos)

    

# def set_skyland_cubes(matrix: list, size: int): # Better change to other logic - starting point, from which cube creates (like incert)
#     shift = int(size - 8)

#     # Boxes
#     for i in range(7):
#         # top-left
#         matrix[i][0] = True
#         matrix[i][6] = True
#         matrix[0][i] = True
#         matrix[6][i] = True
        
#         # top-right
#         matrix[i][shift] = True
#         matrix[i][shift + 6] = True
#         matrix[0][i + shift] = True
#         matrix[6][i + shift] = True

#         # bottom-left
#         matrix[shift + i][0] = True
#         matrix[shift + i][6] = True
#         matrix[shift][i] = True
#         matrix[shift + 6][i] = True
    
#     _inside_shift = 2
#     shift = int(size - 6)
#     # 3x3 inside
#     for i in range(3):
#         ii = i + _inside_shift

#         # top-left
#         matrix[ii][_inside_shift] = True
#         matrix[ii][_inside_shift + 1] = True
#         matrix[ii][_inside_shift + 2] = True

#         # top-right
#         matrix[ii][shift] = True
#         matrix[ii][shift + 1] = True
#         matrix[ii][shift + 2] = True

#         # bottom-left
#         matrix[shift + i][_inside_shift] = True
#         matrix[shift + i][_inside_shift + 1] = True
#         matrix[shift + i][_inside_shift + 2] = True
        

#     print(f"Created Cube in top-left corner")
#     return matrix

if __name__ == "__main__":
    # setup
    version = 1
    size = create_size_by_version(version=version)
    matrix = create_matrix_by_size(size=size)

    # changes
    # centre_cube = get_centre_by_size(size=size)
    matrix = make_changes(matrix=matrix, size=size)

    # preetier
    matrix = set_margins(matrix=matrix, margin_size=1)

    # display
    print_matrix(matrix=matrix)