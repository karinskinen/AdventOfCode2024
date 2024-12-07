import pathlib

with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

start_position = None
start_direction = None

def move(position, direction):
    x, y = position
    if direction == "^":
        return x, y - 1  # Up
    elif direction == ">":
        return x + 1, y  # Right
    elif direction == "v":
        return x, y + 1  # Down
    elif direction == "<":
        return x - 1, y  # Left

def rotate_right(direction):
    directions = ["^", ">", "v", "<"]
    current_index = directions.index(direction)
    return directions[(current_index + 1) % 4]  # Next direction

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell in "^>v<":
            start_position = (x, y)
            start_direction = cell
            break
    if start_position:
        break

print(f"Starting position: {start_position}, direction: {start_direction}")

def simulate_guard(grid, start_position, start_direction):
    position = start_position
    direction = start_direction
    visited_positions = {position}  # Number of unique positions
    rows = len(grid) 
    cols = len(grid[0]) 

    while True:
        # Count the next position
        next_position = move(position, direction)
        x, y = next_position

        # Check if the guard has left the mapped area
        if x < 0 or x >= cols or y < 0 or y >= rows:
            break

        # Check if there is a wall in the next position
        if grid[y][x] == "#":
            # Move 90 degrees to the right
            direction = rotate_right(direction)
        else:
            # Move forward
            position = next_position
            visited_positions.add(position)

    return visited_positions


visited_positions = simulate_guard(grid, start_position, start_direction)
print(f"No of unique positions visited by the guard: {len(visited_positions)}")

# The answer I've gotten was 4454 and it was correct.