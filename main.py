# size = 21
# matrix = (
#     [[None for _ in range(size)] for _ in range(size)]
# )

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

def make_changes(matrix: list):
    set_skyland_cubes()

def set_centre_cube(matrix: list, centre_cube):
    matrix[centre_cube][centre_cube] = True
    print(f"Made change to matrix[{centre_cube}][{centre_cube}]")
    return matrix

def set_skyland_cubes(matrix: list, size: int):
    for i in range(7):
        matrix[i][0] = True
        matrix[i][6] = True
        matrix[0][i] = True
        matrix[6][i] = True
    print(f"Created Cube in top-left corner")
    return matrix






def print_matrix(matrix):
    # _matrix[10][10] = True
    for row in matrix:
        print("".join(("  " if cell != None else "██") for cell in row))
    print("Matrix displayed")


if __name__ == "__main__":
    # setup
    version = 1
    size = create_size_by_version(version=version)
    matrix = create_matrix_by_size(size=size)

    # changes
    # centre_cube = get_centre_by_size(size=size)
    # matrix = make_changes(matrix=matrix, centre_cube=centre_cube)

    # display
    print_matrix(matrix=matrix)