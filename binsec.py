from bisect import bisect_left
import time
import tracemalloc
import os
import psutil

NUM_MULTIPLE_LAUCHES = 10

def binary_search(arr_m: list, arr_n: list) -> int:
    if len(arr_m) == 0 or len(arr_n) == 0:
        return -1

    if len(arr_m) > len(arr_n):
        arr_m, arr_n = arr_n, arr_m

    result = next(
        (elem for elem in arr_m
         if (idx := bisect_left(arr_n, elem)) < len(arr_n) and arr_n[idx] == elem),
        -1
    )
    return result

def binary_search_test(arr_m: list, arr_n: list):
    process = psutil.Process(os.getpid())

    tracemalloc.start()
    before_mem = process.memory_info().rss
    res = binary_search(arr_m, arr_n)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    after_mem = process.memory_info().rss
    memory_used = max(peak / 1024, after_mem - before_mem)  # kbytes

    start = time.perf_counter()
    for _ in range(NUM_MULTIPLE_LAUCHES):
        binary_search(arr_m, arr_n)
    time_spent = (time.perf_counter() - start) / NUM_MULTIPLE_LAUCHES

    return res, time_spent, memory_used