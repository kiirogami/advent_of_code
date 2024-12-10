import numpy as np

FILE = "data/day_10.txt"


def main():
    maze = []
    with open(FILE, "r") as file:
        for line in file:
            row = line.strip()
            maze.append(row)
    maze = np.array([list(row) for row in maze], dtype=int)
    roots = find_roots(maze)

    total_value = 0
    for root in roots:
        nodes = [root]
        while len(nodes) != 0:
            terminated = 0
            nodes_tmp = np.array([])
            for node in nodes:
                if not node.terminate:
                    terminated += 1
                    nodes_tmp = np.append(nodes_tmp, node.move())
                    pass

            # nodes = remove_duplicate(nodes_tmp)   # for part 1
            nodes = nodes_tmp  # for part 2
            if nodes[0].value == 9:
                break
        total_value += len(nodes)
    print(total_value)


def remove_duplicate(arr):
    arr = np.asarray(arr)
    new_arr = []
    for element in arr:
        if element not in new_arr:
            new_arr.append(element)
    return np.asarray(new_arr)


def find_roots(maze):
    roots = []
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y, x] == 0:
                roots.append(Root([y, x], maze))
    return roots


class Root:
    def __init__(self, pos, maze, value=0):
        self.pos = np.array(pos)
        self.maze = maze
        self.current_pos = pos
        self.value = value
        self.terminate = value == 9

    def move(self):
        if self.terminate:
            return [self]
        limits = np.array([len(self.maze), len(self.maze[0])])
        directions = np.array(
            [
                [1, 0],
                [0, 1],
                # [1, 1],
                # [-1, 1],
                [-1, 0],
                [0, -1],
                # [-1, -1],
                # [1, -1],
            ]
        )
        ret = []
        for dir in directions:
            new_pos = self.current_pos + np.array(dir)
            if all(new_pos >= 0) and all(new_pos < limits):
                y, x = new_pos
                if self.maze[y][x] == self.value + 1:
                    new_node = Root(new_pos, self.maze, self.value + 1)
                    ret.append(new_node)
            else:
                continue
        return ret

    def __eq__(self, other):
        return np.array_equal(self.pos, other.pos) and (self.value == other.value)

    def __hash__(self):
        return hash(np.concatenate(self.pos, [self.value]).tobytes())


if __name__ == "__main__":
    main()
