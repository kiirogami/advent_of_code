import numpy as np

FILE_PATH = "data/day_06.txt"


def main():
    maze = []
    with open(FILE_PATH, "r") as file:
        for line in file:
            row = line.strip()
            maze.append(row)
    list_maze = np.array([list(row) for row in maze])
    agent = Agent(list_maze)
    agent.move()
    print(agent.visited_pos)
    print(agent.loop_amount())


class VisitedNode:
    def __init__(self, position, direction) -> None:
        self.position = position
        self.visited_conditions = []
        self.visited_conditions.append(direction.tolist())

    def visited(self, direction):
        if direction in self.visited_conditions:
            return True
        else:
            self.visited_conditions.append(direction.tolist())
            return False


class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.init_maze = np.copy(maze)
        self.find_agent()
        self.maze_dims = np.array([len(self.maze), len(self.maze[0])])
        self.visited_pos = 1
        self.init_pos = np.copy(self.position)
        self.path = []
        self.path_pos = []

    def find_agent(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] in ">v^<":
                    self.position = np.array([y, x])
                    match self.maze[y][x]:
                        case ">":  # (y,x)
                            self.direction = np.array([0, 1])
                        case "v":
                            self.direction = np.array([1, 0])
                        case "^":
                            self.direction = np.array([-1, 0])
                        case "<":
                            self.direction = np.array([0, -1])
                    return

    def rotate_90(self):
        self.direction = np.array([[0, 1], [-1, 0]]) @ self.direction

    def move(self, part2=False):
        moving = True
        y, x = self.position
        self.maze[y][x] = "X"
        while moving:
            new_position = self.position + self.direction
            y, x = new_position
            if all(new_position < self.maze_dims) and all(new_position >= 0):

                if self.maze[y][x] in ".X":
                    if part2:
                        if new_position.tolist() in self.path_pos:
                            if self.is_stuck(new_position):
                                return -1

                    if self.maze[y][x] == ".":
                        self.visited_pos += 1
                    self.maze[y][x] = "X"
                    self.path.append(VisitedNode(new_position, self.direction))
                    self.path_pos.append(new_position.tolist())
                    self.position = new_position
                elif self.maze[y][x] == "#":
                    self.rotate_90()
            else:
                moving = False
        return self.visited_pos

    def is_stuck(self, position):
        p = np.copy(position).tolist()
        for node in self.path:
            if np.array_equal(p, node.position):
                if self.direction.tolist() in node.visited_conditions:
                    return True
        else:
            return False

    def loop_amount(self):
        self._remove_copies()
        loop_amount = 0
        for pos in self.path:
            new_maze = np.copy(self.init_maze)
            if np.array_equal(pos.position, self.init_pos):
                continue
            new_maze[pos.position[0]][pos.position[1]] = "#"
            agent = Agent(new_maze)
            if agent.move(True) == -1:
                loop_amount += 1
        return loop_amount

    def _remove_copies(self):
        new_list = []
        pos_list = []
        for node in self.path:
            if node.position.tolist() in pos_list:
                continue
            else:
                new_list.append(node)
                pos_list.append(node.position.tolist())
        self.path = new_list


if __name__ == "__main__":
    main()
