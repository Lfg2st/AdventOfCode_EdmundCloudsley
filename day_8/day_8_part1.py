import math
import time

root_start_time = time.time()

with open('AdventOfCode_EdmundCloudsley/day_8/test.txt', 'r') as f:
    txt = f.read().splitlines()
print(f'Parsing time: {time.time() - root_start_time} seconds', )
processing_start_time = time.time()

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

def find_antinodes(coord_1, coord_2):
    """
    Given two coordinates, calculate the two potential antinode points that are symmetric across the midpoint.
    
    Args:
        coord_1 (tuple): First coordinate (x1, y1).
        coord_2 (tuple): Second coordinate (x2, y2).
    
    Returns:
        tuple: The two calculated antinode points:
               - Point 1: (x3, y3), 2 times the distance from (x2, y2) towards (x1, y1)
               - Point 2: (x4, y4), 2 times the distance from (x1, y1) towards (x2, y2)
    """
    x1, y1 = coord_1
    x2, y2 = coord_2
    x3 = 2 * x1 - x2
    y3 = 2 * y1 - y2
    x4 = 2 * x2 - x1
    y4 = 2 * y2 - y1
    
    return (x3, y3), (x4, y4)

antinodes = set()
mat_txt = mat_populator(txt=txt)

MAX_ROW = len(mat_txt) - 1
MIN_ROW = 0

MAX_COL = len(mat_txt[0]) - 1
MIN_COL = 0

tower_coords_list, tower_coords = tower_coord_finder(mat_txt)

for frequency, coords in tower_coords.items():
    for index, coord_1 in enumerate(coords):
        if index != len(coords) - 1:
            for index2 in range(index + 1, len(coords)):
                coord_2 = coords[index2]
                anti_node_1, anti_node_2 = find_antinodes(coord_1, coord_2)

                if is_within_bounds(anti_node_1, MAX_ROW, MAX_COL) and anti_node_1 not in tower_coords_list:
                    antinodes.add(anti_node_1)
                if is_within_bounds(anti_node_2, MAX_ROW, MAX_COL) and anti_node_2 not in tower_coords_list:
                    antinodes.add(anti_node_2)
print("---------")
print(f"Processing time: {time.time() - processing_start_time} seconds")
print("---------")
print(f"Total time: {time.time() - root_start_time}")
print("---------")
print(f"Number of antinodes: {len(antinodes)}")
