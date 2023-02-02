import random
from functools import reduce
import time


def timeit(func, n=100000, repetition=10):
    times = []
    for seed in range(repetition):
        arr = list(range(n))
        random.seed(seed)
        random.shuffle(arr)

        start = time.perf_counter()
        func(arr)
        end = time.perf_counter() - start

        times.append(end)

    print(times)
    avg_time = sum(times) / len(times)
    std_time = (
        reduce(lambda a, b: a + b, map(lambda x: (x - avg_time) ** 2, times))
        / (len(times) - 1)
    ) ** 0.5
    print(f"Avg time: {avg_time:.2f} ± {std_time:.2f} s")


if __name__ == "__main__":
    from time_counter import timeit

    arr = [3, 2, 5, 4, 3, 12, 32, -2, 34, -54, 22]
    sorted_arr = sorted(arr)
    print(sorted_arr)

    timeit(sorted)
