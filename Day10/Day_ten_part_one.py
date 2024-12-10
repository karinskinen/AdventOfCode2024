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

def find_reachable_nines(start):
    queue = deque([start])
    visited = set()
    reachable_nines = set()

    while queue:
        r, c = queue.popleft()
        visited.add((r, c))

        current_height = topographic_map[r][c]

        if current_height == 9:
            reachable_nines.add((r, c))
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                new_height = topographic_map[new_r][new_c]

                if new_height == current_height + 1:
                    queue.append((new_r, new_c))

    return reachable_nines

def main():
    trailheads = find_trailheads()
    total_score = 0

    for trailhead in trailheads:
        reachable_nines = find_reachable_nines(trailhead)
        total_score += len(reachable_nines)

    print(f"The sum of all the trailheads scores: {total_score}")

main()

# I got a 611 as a result. I will now try to solve the second part of the problem.