import numpy as np

FILE = "data/day_12_test.txt"
FILE = "data/day_12.txt"


def main():

    garden = []
    with open(FILE, "r") as file:
        for line in file:
            row = list(line.strip())
            garden.append(row)

    groups, id_amount = garden_to_unique_ids(garden)
    perimeters = calculate_perimeters(groups)
    result = 0

    for key in perimeters:
        # print(f"{key}, {perimeters[key]}x{id_amount[key]}")
        result += perimeters[key] * id_amount[key]
    print(result)


def garden_to_unique_ids(garden):
    rows, cols = len(garden), len(garden[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    id_grid = [[np.nan for _ in range(cols)] for _ in range(rows)]
    current_id = 0

    def flood_fill(y, x, key, id):
        if y < 0 or y >= rows or x < 0 or x >= cols:
            return
        if visited[y][x] or garden[y][x] != key:
            return
        visited[y][x] = True
        id_grid[y][x] = id
        flood_fill(y + 1, x, key, id)
        flood_fill(y - 1, x, key, id)
        flood_fill(y, x + 1, key, id)
        flood_fill(y, x - 1, key, id)

    for y in range(rows):
        for x in range(cols):
            if not visited[y][x]:
                flood_fill(y, x, garden[y][x], current_id)
                current_id += 1
    id_amounts = {}

    id_grid = np.asarray(id_grid)
    for id in range(current_id):
        id_amounts[id] = len(np.where(id_grid == id)[0])
    return id_grid, id_amounts


def calculate_perimeters(grid):
    rows, cols = len(grid), len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    perimeters = {}

    for r in range(rows):
        for c in range(cols):
            id = grid[r][c]
            if id not in perimeters:
                perimeters[id] = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != id:
                    perimeters[id] += 1

    return dict(perimeters)


if __name__ == "__main__":
    main()
