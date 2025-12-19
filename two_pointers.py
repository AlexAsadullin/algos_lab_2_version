import time
import tracemalloc
import os
import psutil

NUM_MULTIPLE_LAUCHES = 10

def two_pointers(arr_m: list, arr_n: list) -> int:
    i, j = 0, 0
    while i < len(arr_m) and j < len(arr_n):
        if arr_m[i] == arr_n[j]:
            return arr_m[i]
        elif arr_m[i] < arr_n[j]:
            i += 1
        else:
            j += 1
    return -1

def two_pointers_test(arr_m: list, arr_n: list):
    process = psutil.Process(os.getpid())

    tracemalloc.start()
    before_mem = process.memory_info().rss
    res = two_pointers(arr_m, arr_n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    after_mem = process.memory_info().rss
    memory_used = max(peak / 1024, after_mem - before_mem)  # kbytes

    start = time.perf_counter()
    for _ in range(NUM_MULTIPLE_LAUCHES):
        two_pointers(arr_m, arr_n)
    time_spent = (time.perf_counter() - start) / NUM_MULTIPLE_LAUCHES

    return res, time_spent, memory_used