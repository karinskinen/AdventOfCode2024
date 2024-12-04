import pathlib

word = "XMAS"

def read_file(input_filename):
    with open(f"{pathlib.Path(__file__).parent.resolve()}/{input_filename}", "r") as file:
        grid = [list(line.strip()) for line in file]
    return grid

def find_xmas(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Anti-diagonal down-left
        (-1, 1),  # Anti-diagonal up-right
    ]
    count = 0

    def is_word_at(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return False
        return True

    # Search for the word in all directions
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if is_word_at(r, c, dr, dc):
                    count += 1

    return count

grid = read_file("input_day4.txt")

result = find_xmas(grid, word)
print(f"The word '{word}' appears {result} times in the grid.")

