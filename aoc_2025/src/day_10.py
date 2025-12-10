import numpy as np
import ast
from collections import deque
import time

PATH = "data/day_10_easy.txt"
PATH = "data/day_10.txt"


class Light:
    def __init__(self, light_req, buttons, joltage_req):
        self.light_req = light_req
        self.buttons = buttons
        self.joltage_req = joltage_req
        self.lights = np.zeros_like(self.light_req, dtype=bool)
        self.joltages = np.zeros_like(self.light_req, dtype=int)


def main():
    data = load_txt(PATH)
    print(part1(data))
    s = time.time()
    print(part2(data))
    print("part 2 runtime:", (time.time() - s))
    pass


def part1(lights):
    steps = 0
    for light in lights:
        steps += solve_puzzle_part1(light)
    return steps


def part2(lights):
    steps = 0
    for light in lights:
        steps += solve_puzzle_part2(light)
    return steps


def solve_puzzle_part1(light: Light):
    # bfs
    start_t = tuple(light.lights.tolist())
    goal_t = tuple(light.light_req.tolist())

    parents = {start_t: None}
    visited = {start_t}
    queue = deque([start_t])
    while queue:
        curr = queue.popleft()
        if curr == goal_t:
            break
        for i, button in enumerate(light.buttons):
            new_state = np.logical_xor(curr, button).astype(int).tolist()
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                parents[new_state] = (curr, i)
                queue.append(new_state)

    if goal_t not in parents:
        return None

    sequence = []
    x = goal_t
    while x != start_t:
        prev, button_idx = parents[x]
        sequence.append(button_idx)
        x = prev
    sequence.reverse()
    return len(sequence)


def solve_puzzle_part2(light: Light):
    # bfs, hahahaha, not gonna run that
    start_t = tuple(light.joltages.tolist())
    goal_t = tuple(light.joltage_req.tolist())

    parents = {start_t: None}
    visited = {start_t}
    queue = deque([start_t])
    while queue:
        curr = queue.popleft()
        if curr == goal_t:
            break
        for i, button in enumerate(light.buttons):
            new_state = np.add(curr, button).astype(int).tolist()
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                parents[new_state] = (curr, i)
                queue.append(new_state)

    if goal_t not in parents:
        return None

    sequence = []
    x = goal_t
    while x != start_t:
        prev, button_idx = parents[x]
        sequence.append(button_idx)
        x = prev
    sequence.reverse()
    return len(sequence)


def load_txt(path):
    try:
        with open(path, "r") as file:
            full_text_string = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return np.array([])
    rows = full_text_string.splitlines()
    lights = []
    for row in rows:
        row = row.split(" ")

        light_req = row[0]
        light_req = np.array(list(light_req.strip("[]")), dtype="<U1")
        light_req = light_req == "#"

        buttons_data = row[1:-1]
        buttons = []
        for b in buttons_data:
            b = np.array(ast.literal_eval(b))
            action = np.zeros_like(light_req, dtype=bool)
            action[b] = True
            buttons.append(action)
        buttons = np.asarray(buttons)

        joltage_req = np.array(ast.literal_eval(row[-1].strip("{}")))

        lights.append(Light(light_req, buttons, joltage_req))
    return lights


if __name__ == "__main__":
    main()
