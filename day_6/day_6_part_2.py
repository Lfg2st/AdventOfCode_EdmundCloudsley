import time

start_time = time.time()

def move_forward(mat, row, col, orientation):
    """Returns the updated matrix and position if movement is successful; 
    else returns the updated orientation after turning 90 degrees."""

    if orientation == 0:  
        if row > 0 and mat[row - 1][col] != "#":  
            mat[row][col], mat[row - 1][col] = mat[row - 1][col], mat[row][col]
            return mat, row - 1, col, orientation
        else:
            return mat, row, col, (orientation + 1) % 4  

    elif orientation == 1:  
        if col < len(mat[row]) - 1 and mat[row][col + 1] != "#":  
            mat[row][col], mat[row][col + 1] = mat[row][col + 1], mat[row][col]
            return mat, row, col + 1, orientation
        else:
            return mat, row, col, (orientation + 1) % 4  

    elif orientation == 2:  
        if row < len(mat) - 1 and mat[row + 1][col] != "#":  
            mat[row][col], mat[row + 1][col] = mat[row + 1][col], mat[row][col]
            return mat, row + 1, col, orientation
        else:
            return mat, row, col, (orientation + 1) % 4  

    elif orientation == 3:  
        if col > 0 and mat[row][col - 1] != "#":  
            mat[row][col], mat[row][col - 1] = mat[row][col - 1], mat[row][col]
            return mat, row, col - 1, orientation
        else:
            return mat, row, col, (orientation + 1) % 4  

    return mat, row, col, orientation

def create_mat_versions(mat):
    """Create versions of the matrix with each '.' replaced by '#' systematically."""
    mat_versions = []
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == ".":  
                new_mat = [row[:] for row in mat]  
                new_mat[r][c] = "#"  
                mat_versions.append(new_mat)  
    return mat_versions

def detect_loops(mat, turtle_row, turtle_col, orientation):
    """Simulate turtle movement and detect if a loop is created."""
    visited_positions = set()
    visited_positions.add((turtle_row, turtle_col, orientation))

    while True:
        mat, turtle_row, turtle_col, orientation = move_forward(mat, turtle_row, turtle_col, orientation)

        if (turtle_row, turtle_col, orientation) in visited_positions:
            return True  

        visited_positions.add((turtle_row, turtle_col, orientation))

        if orientation == 0 and turtle_row == 0:  
            break
        elif orientation == 1 and turtle_col == len(mat[turtle_row]) - 1:  
            break
        elif orientation == 2 and turtle_row == len(mat) - 1:  
            break
        elif orientation == 3 and turtle_col == 0:  
            break

    return False  

file_name = 'day_6/input.txt'

with open(file_name, "r") as f:
    txt = f.read().splitlines()

mat = []

for line in txt:
    row = list(line)
    mat.append(row)

for r, row in enumerate(mat):
    for c, char in enumerate(row):
        if char == "^":
            turtle_col = c
            turtle_row = r
            orientation = 0
            break

mat_versions = create_mat_versions(mat)

loop_creator = 0

for version in mat_versions:
    if detect_loops(version, turtle_row, turtle_col, orientation):
        loop_creator += 1
print('Time elapsed: ', time.time() - start_time)
print("Number of loops detected:", loop_creator)