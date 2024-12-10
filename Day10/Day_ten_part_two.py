from collections import deque
import pathlib

with open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", "r") as file:
    topographic_map = [
        list(map(int, line.strip()))
        for line in file.readlines()
    ]

rows = len(topographic_map)
cols = len(topographic_map[0])

def find_trailheads():
    trailheads = []
    for r in range(rows):
        for c in range(cols):
            if topographic_map[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def find_distinct_trails(start):
    queue = deque([(start, [start])])  # Varje element är (position, ledens väg)
    distinct_trails = set()

    while queue:
        (r, c), path = queue.popleft()
        current_height = topographic_map[r][c]

        # Om vi når en 9:a, lägg till vägen som en distinkt led
        if current_height == 9:
            distinct_trails.add(tuple(path))
            continue

        # Undersök grannar
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                next_height = topographic_map[nr][nc]
                if next_height == current_height + 1 and (nr, nc) not in path:
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return distinct_trails

def main():
    trailheads = find_trailheads()
    total_rating = 0

    for trailhead in trailheads:
        distinct_trails = find_distinct_trails(trailhead)
        total_rating += len(distinct_trails)

    print(f"The sum of all the trailheads scores: {total_rating}")

main()

# I got 1380 as a result and it was correct
