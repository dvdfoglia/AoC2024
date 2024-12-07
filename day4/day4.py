def read_input(file_path):
    with open(file_path, 'r') as input_file:
        return [list(line) for line in input_file.read().splitlines()]

data = read_input("data.txt")

directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (1, 1), (-1, -1), (1, -1), (-1, 1)
]

xmas_configurations = [
    # M at top-left, top-right
    [(-1, -1, 'M'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'S')],
    # M at bottom-left, bottom-right
    [(1, -1, 'M'), (1, 1, 'M'), (-1, -1, 'S'), (-1, 1, 'S')],
    # M at top-left, bottom-left
    [(-1, -1, 'M'), (1, -1, 'M'), (-1, 1, 'S'), (1, 1, 'S')],
    # M at top-right, bottom-right
    [(-1, 1, 'M'), (1, 1, 'M'), (-1, -1, 'S'), (1, -1, 'S')],
]

def check_word(grid, row, col, direction):
    word = "XMAS"
    for i, char in enumerate(word):
        r, c = row + direction[0] * i, col + direction[1] * i
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != char:
            return False
    return True

def check_pattern(grid, row, col, configuration):
    for dr, dc, char in configuration:
        r, c = row + dr, col + dc
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != char:
            return False
    return True

word_count = 0
pattern_count = 0

for row in range(len(data)):
    for col in range(len(data[row])):
        # Check for "XMAS" word
        for direction in directions:
            if check_word(data, row, col, direction):
                word_count += 1

        # Check for X-MAS patterns centered at 'A'
        if data[row][col] == 'A':
            for configuration in xmas_configurations:
                if check_pattern(data, row, col, configuration):
                    pattern_count += 1

print(f"Part1: {word_count}")
print(f"Part2: {pattern_count}")
