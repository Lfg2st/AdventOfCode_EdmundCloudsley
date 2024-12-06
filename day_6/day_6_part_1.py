import time


start_time = time.time()
def move_forward(mat, row, col, orientation):
    """Returns the updated matrix and position if movement is successful; 
    else returns the updated orientation after turning 90 degrees."""
    
    # Try moving, and handle turns if an obstacle is present
    if orientation == 0:  # Pointing upwards
        if row > 0 and mat[row - 1][col] != "#":  # Can move up
            mat[row][col], mat[row - 1][col] = mat[row - 1][col], mat[row][col]
            return mat, row - 1, col, orientation
        else:
            return mat, row, col, (orientation + 1) % 4  # Turn right
    
    elif orientation == 1:  # Pointing to the right
        if col < len(mat[row]) - 1 and mat[row][col + 1] != "#":  # Can move right
            mat[row][col], mat[row][col + 1] = mat[row][col + 1], mat[row][col]
            return mat, row, col + 1, orientation
        else:
            return mat, row, col, (orientation + 1) % 4  # Turn right

    elif orientation == 2:  # Pointing downward
        if row < len(mat) - 1 and mat[row + 1][col] != "#":  # Can move down
            mat[row][col], mat[row + 1][col] = mat[row + 1][col], mat[row][col]
            return mat, row + 1, col, orientation
        else:
            return mat, row, col, (orientation + 1) % 4  # Turn right

    elif orientation == 3:  # Pointing to the left
        if col > 0 and mat[row][col - 1] != "#":  # Can move left
            mat[row][col], mat[row][col - 1] = mat[row][col - 1], mat[row][col]
            return mat, row, col - 1, orientation
        else:
            return mat, row, col, (orientation + 1) % 4  # Turn right

    return mat, row, col, orientation

def mat_to_string(mat):
    return '\n'.join([''.join(row) for row in mat])

visited_dots = set()

file_name = 'day_6/input.txt'

with open(file_name, "r") as f:
    txt = f.read().splitlines()

mat = []

# Populate the matrix
for line in txt:
    row = []
    for char in list(line):
        row.append(char)
    mat.append(row)

# Find the initial position of the turtle
for row, i in enumerate(mat):
    for col, j in enumerate(i):
        if j == "^":
            turtle_col = col
            turtle_row = row
            orientation = 0  
            break


visited_dots.add((turtle_row, turtle_col))


while True:
    mat, turtle_row, turtle_col, orientation = move_forward(mat, turtle_row, turtle_col, orientation)
    

    visited_dots.add((turtle_row, turtle_col))
    

    if orientation == 0 and turtle_row == 0:  # Reached the first row (upwards)
        break
    elif orientation == 1 and turtle_col == len(mat[turtle_row]) - 1:  # Reached the last column (right)
        break
    elif orientation == 2 and turtle_row == len(mat) - 1:  # Reached the last row (downwards)
        break
    elif orientation == 3 and turtle_col == 0:  # Reached the first column (left)
        break




# Output the result
print("Number of distinct positions visited:", len(visited_dots), time.time() - start_time)
