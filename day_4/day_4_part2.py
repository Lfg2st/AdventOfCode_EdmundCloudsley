def get_input(fp):
    with open(fp, 'r') as f:
        input_data = [line.strip('\n') for line in f.readlines()]
    return input_data


def get_xmas_combos(posx, posy, text):
    level = [0, 0, 0, 0]
    up = [0, 1, 2, 3]
    down = [0, -1, -2, -3]
    
    up_right = list(zip(up, down))
    up_left = list(zip(down, down))
    x_up = list(zip(level, down))
    left = list(zip(down, level))
    right = list(zip(up, level))
    x_down = list(zip(level, up))
    down_right = list(zip(up, up))
    down_left = list(zip(down, up))

    xmas_combos = []
    for combo in [up_right, up_left, x_up, left, right, x_down, down_left, down_right]:
        xmas_combos.append("".join([(text[posy+y][posx+x]) for x, y in combo]))

    return [x for x in xmas_combos if x == 'XMAS']


def get_mas_combos(posx, posy, text):
    matches = [['SAM', 'SAM'], ['MAS', 'MAS'], ['SAM', 'MAS'], ['MAS', 'SAM']]

    d1 = [-1, 0, 1]
    d2 = [1, 0, -1]
    diag1 = list(zip(d1, d2))
    diag2 = list(zip(d1, d1))

    mas_combos = []
    for combo in [diag1, diag2]:
        mas_combos.append("".join([(text[posy+y][posx+x]) for x, y in combo]))

    if mas_combos in matches:
        return ["_".join(mas_combos )]

    return []


def part1(text):
    text_extended = [row + 'OOOO' for row in text + 4 * [len(text[0]) * 'O']]
    filtered_input = [y for newrow in [get_xmas_combos(i, j, text_extended) for j, row in enumerate(text_extended) for i, x in enumerate(row) if x == 'X'] for y in newrow]

    return len(filtered_input)


def part2(text):
    text_extended = [row + 'OOOO' for row in text + 4 * [len(text[0]) * 'O']]
    filtered_input = [y for newrow in [get_mas_combos(i, j, text_extended) for j, row in enumerate(text_extended) for i, x in enumerate(row) if x == 'A'] for y in newrow]
    return len(filtered_input)


print('Part 1', part1(get_input("day_4/grid.txt")))
print('Part 2', part2(get_input("day_4/grid.txt")))