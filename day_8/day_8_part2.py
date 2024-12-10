import math

# Data Ingestion
with open('day_8/input.txt', 'r') as f:
    txt = f.read().splitlines()

def is_within_bounds(p, max_row, max_col):
    """
    Check if a given point (p) is within the bounds of the matrix.
    
    Args:
        p (tuple): A tuple representing the point (x, y).
        max_row (int): The maximum row index in the matrix.
        max_col (int): The maximum column index in the matrix.
    
    Returns:
        bool: True if the point is within the bounds, False otherwise.
    """
    x, y = p
    return 0 <= x <= max_row and 0 <= y <= max_col

def mat_to_string(mat):
    """
    Converts a 2D matrix of characters into a formatted string representation.
    
    Args:
        mat (list of list of str): The 2D matrix to be converted.
    
    Returns:
        str: A string where each row of the matrix is joined by newlines.
    """
    return '\n'.join([''.join(row) for row in mat])

def tower_coord_finder(mat):
    """
    Finds unique non-dot characters and their coordinates in a 2D matrix.
    
    Args:
        mat (list of list of str): The 2D matrix to analyze.
    
    Returns:
        tuple: A list of all coordinates where a tower exists (excluding '.'),
               and a dictionary mapping each unique tower character to a list of its coordinates.
    """
    tower_coords_list = []
    tower_coords = {}
    unique_towers = []

    for idx_row, row in enumerate(mat):
        for idx_col, item in enumerate(row):
            if item != '.':
                tower_coords_list.append((idx_row, idx_col))
                if item not in unique_towers:
                    unique_towers.append(item)
                    tower_coords[item] = [(idx_row, idx_col)]
                else:
                    tower_coords[item].append((idx_row, idx_col))

    return tower_coords_list, tower_coords

def mat_populator(txt):
    """
    Converts a list of strings into a 2D matrix of characters.
    
    Args:
        txt (list of str): A list of strings representing the rows of the matrix.
    
    Returns:
        list of list of str: A 2D matrix (list of lists) where each character is an element in a row.
    """
    mat = []
    for line in txt:
        row = []
        for char in list(line):
            row.append(char)
        mat.append(row)
    return mat

def find_collinear_points(coord_1, coord_2, tower_coords_list):
    """
    Given two coordinates, find all collinear points in the same row or column.
    
    Args:
        coord_1 (tuple): First coordinate (x1, y1).
        coord_2 (tuple): Second coordinate (x2, y2).
        tower_coords_list (list): List of all coordinates where towers are located.
    
    Returns:
        list: A list of all collinear points along the row or column of coord_1 and coord_2.
    """
    collinear_points = []
    x1, y1 = coord_1
    x2, y2 = coord_2
    
    # Check for collinearity in the same row or column
    if x1 == x2:  # Same row
        for x, y in tower_coords_list:
            if x == x1:
                collinear_points.append((x, y))
    elif y1 == y2:  # Same column
        for x, y in tower_coords_list:
            if y == y1:
                collinear_points.append((x, y))
    
    return collinear_points

antinodes = set()
mat_txt = mat_populator(txt=txt)

MAX_ROW = len(mat_txt) - 1
MIN_ROW = 0

MAX_COL = len(mat_txt[0]) - 1
MIN_COL = 0

tower_coords_list, tower_coords = tower_coord_finder(mat_txt)

for frequency, coords in tower_coords.items():
    # Add the towers themselves as antinodes if they are in line with at least one other tower of the same frequency
    for coord_1 in coords:
        collinear_points = find_collinear_points(coord_1, coord_1, coords)  # At least itself should be in line
        if len(collinear_points) > 1:
            for point in collinear_points:
                if is_within_bounds(point, MAX_ROW, MAX_COL):
                    antinodes.add(point)  # Add the point to antinodes if within bounds

    # Now, consider all pairs of towers and find collinear points between them
    for index, coord_1 in enumerate(coords):
        for index2 in range(index + 1, len(coords)):
            coord_2 = coords[index2]
            collinear_points = find_collinear_points(coord_1, coord_2, tower_coords_list)
            
            for point in collinear_points:
                if is_within_bounds(point, MAX_ROW, MAX_COL):
                    antinodes.add(point)

print(len(antinodes))
