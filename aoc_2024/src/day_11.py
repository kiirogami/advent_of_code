import numpy as np
import time

FILE = "data/day_11_test.txt"
FILE = "data/day_11.txt"

stones_iter = {}


def main():
    stones = np.loadtxt(FILE, dtype=int)

    full_time = 0

    unique_stones = np.unique(stones)
    stones_amount = {}
    stones_iter_result = {}
    for u_stone in unique_stones:
        stones_amount[u_stone] = len(np.where(stones == u_stone)[0])

    for _ in range(25):
        s = time.time()

        for stone in stones_amount:
            if stone not in stones_iter:
                stones_iter[stone] = blink_single_stone(stone, 3)
                stones_iter_result[stone] = stones_iter[stone]
            else:
                stones_iter_result[stone] = stones_iter[stone]

        new_amounts = {}
        for key in stones_iter_result:
            unique_stones = np.unique(stones_iter_result[key])
            for u_stone in unique_stones:
                if u_stone not in new_amounts:
                    new_amounts[u_stone] = (
                        len(np.where(stones_iter_result[key] == u_stone)[0])
                        * stones_amount[key]
                    )
                else:
                    new_amounts[u_stone] += (
                        len(np.where(stones_iter_result[key] == u_stone)[0])
                        * stones_amount[key]
                    )
        stones_amount = new_amounts
        stones_iter_result = {}

        e = time.time()
        t = e - s
        full_time += t
        print(t, "s")

    print("--------------------------")
    print(full_time)
    result = 0
    for stone in stones_amount:
        result += stones_amount[stone]
    print(result)


# faster
def blink_single_stone(value, amount):
    stones = np.array([value])
    for _ in range(amount):
        new_stones = np.array([])
        for stone in stones:
            if stone == 0:
                new_stones = np.append(new_stones, 1)
            elif len(str(stone)) % 2 == 0:
                str_stone = str(stone)
                len_stone = len(str_stone)
                new_stones = np.append(new_stones, int(str_stone[: len_stone // 2]))
                new_stones = np.append(new_stones, int(str_stone[len_stone // 2 :]))
            else:
                new_stones = np.append(new_stones, stone * 2024)
        stones = np.asarray(new_stones, dtype=int)
    return stones


if __name__ == "__main__":
    main()
