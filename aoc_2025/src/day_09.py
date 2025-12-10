import numpy as np
from matplotlib.path import Path

PATH = "data/day_09.txt"
PATH = "data/day_09_easy.txt"


def main():
    data = np.genfromtxt(PATH, dtype=str, delimiter=1)
    print(f"part1: {part1(data)}")
    # print(f"part2: {part2(data)}")


def part2(data):
    get_boundaries(data)
    # ????????????????


def get_boundaries(points):
    boundaries = np.full((1, 2), np.nan)
    for i in range(points.shape[0] - 1):
        y, x = points[i]
        target_points = points[(i + 1) :]
        valid_mask = (target_points[:, 0] == y) | (target_points[:, 1] == x)
        valid_points = target_points[valid_mask]
        boundaries = np.vstack([boundaries, [y, x], valid_points])
    boundaries = boundaries[1:]
    boundaries = np.unique(boundaries, axis=0)
    return boundaries


def part1(data):
    points = np.copy(data)
    max_areas = []
    for i in range(points.shape[0] - 1):
        current = points[i]
        target_points = points[(i + 1) :]
        vecs = np.abs(target_points - current)
        areas = (vecs[:, 0] + 1) * (vecs[:, 1] + 1)
        local_max = np.max(areas)
        max_areas.append(local_max)
    return np.max(max_areas)


if __name__ == "__main__":
    main()
