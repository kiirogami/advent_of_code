import numpy as np

PATH = "data/day_08_easy.txt"
PATH = "data/day_08.txt"


def main():
    data = np.loadtxt(PATH, dtype=int, delimiter=",")
    # print(f"part1: {part1(data, 1000)}")
    print(f"part2: {part2(data)}")


class Circuit:
    def __init__(self):
        self.boxes_ids = set()
        self.length = 0

    def len(self):
        return len(self.boxes_ids)

    def contains(self, id):
        return id in self.boxes_ids

    def add(self, id):
        self.boxes_ids.add(id)


def part2(data):
    data = np.asarray(data)
    amount = data.shape[0]
    # cost, neighbour
    distances = []

    for i in range(amount):
        curr = data[i]
        rows = np.arange(i + 1, amount)
        dists = np.linalg.norm(curr - data[rows], axis=1)
        dist_table = np.array((np.full((amount - (i + 1)), i), rows, dists)).T
        distances = np.append(distances, dist_table)
    distances = distances.reshape((len(distances) // 3, 3))

    dist_idxs_sorted = np.argsort(distances[:, 2])
    circuits = []

    last = None
    for i in dist_idxs_sorted:
        idx = distances[i][0]
        parent_idx = distances[i][1]
        circuits, valid_last = connect(circuits, idx, parent_idx)
        if valid_last:
            last = (idx, parent_idx)
        if circuits[0].len == amount:
            break

    last = np.asarray(last, dtype=int)
    x1, x2 = data[last][:, 0]
    return x1 * x2


def part1(data, connections_req):
    data = np.asarray(data)
    amount = data.shape[0]
    # cost, neighbour
    distances = []

    for i in range(amount):
        curr = data[i]
        rows = np.arange(i + 1, amount)
        dists = np.linalg.norm(curr - data[rows], axis=1)
        dist_table = np.array((np.full((amount - (i + 1)), i), rows, dists)).T
        distances = np.append(distances, dist_table)
    distances = distances.reshape((len(distances) // 3, 3))

    dist_idxs_sorted = np.argsort(distances[:, 2])
    circuits = []

    connections_req = 1000
    for i in dist_idxs_sorted[:connections_req]:
        idx = distances[i][0]
        parent_idx = distances[i][1]
        circuits, _ = connect(circuits, idx, parent_idx)

    circuits = sorted(circuits, key=lambda x: x.len(), reverse=True)
    lengths = [circuits[i].len() if i < len(circuits) else 1 for i in range(3)]
    result = np.prod(lengths)
    return result


def connect(circuits, id1, id2):
    circ_id1 = in_circuit(circuits, id1)
    circ_id2 = in_circuit(circuits, id2)
    if circ_id1 is None and circ_id2 is None:
        circuit = Circuit()
        circuit.add(id1)
        circuit.add(id2)
        circuits.append(circuit)
        return circuits, False
    # both in same circuit, already connected
    elif circ_id1 == circ_id2:
        return circuits, False
    # only one in different circuit
    elif circ_id1 == None and circ_id2 >= 0:
        circuits[circ_id2].add(id1)
        return circuits, True
    elif circ_id2 == None and circ_id1 >= 0:
        circuits[circ_id1].add(id2)
        return circuits, True
    else:
        # both in different circuits, merge them into one
        for id in circuits[circ_id2].boxes_ids:
            circuits[circ_id1].add(id)
        circuits.pop(circ_id2)
        return circuits, True


def in_circuit(circuits, id):
    for i, c in enumerate(circuits):
        if c.contains(id):
            return i
    else:
        return None


if __name__ == "__main__":
    main()
