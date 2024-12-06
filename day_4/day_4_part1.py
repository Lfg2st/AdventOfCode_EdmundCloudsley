def count_xmas_occurrences(filename, word="XMAS"):
    # Read the grid from the file
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    # Function to check if a word exists starting at (r, c) in a given direction
    def check_direction(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return False
        return True

    # Directions: (dr, dc) tuples
    directions = [
        (0, 1),   # Horizontal (right)
        (0, -1),  # Horizontal (left)
        (1, 0),   # Vertical (down)
        (-1, 0),  # Vertical (up)
        (1, 1),   # Diagonal (down-right)
        (-1, -1), # Diagonal (up-left)
        (1, -1),  # Diagonal (down-left)
        (-1, 1),  # Diagonal (up-right)
    ]

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count

# Specify the file containing the grid
filename = "day_4/grid.txt"

# Count occurrences of "XMAS"
result = count_xmas_occurrences(filename)
print("Total occurrences of 'XMAS':", result)
