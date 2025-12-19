import time
import tracemalloc
import os
import psutil

NUM_MULTIPLE_LAUCHES = 10

def binary_divide(arr_m:list, arr_n:list) -> int:
    def _has_common(i1, j1, i2, j2):
        if i1 >= j1 or i2 >= j2:
            return False
        mid = (i1 + j1) // 2
        val = arr_m[mid]
        l, r = i2, j2 - 1
        while l <= r:
            m = (l + r) // 2
            if arr_n[m] == val:
                return True
            elif arr_n[m] < val:
                l = m + 1
            else:
                r = m - 1
        pos = l
        if _has_common(i1, mid, i2, pos):
            return True
        if _has_common(mid + 1, j1, pos, j2):
            return True
        return False

    res = _has_common(0, len(arr_m), 0, len(arr_n))
    return res


def binary_divide_test(arr_m: list, arr_n: list):
    process = psutil.Process(os.getpid())

    tracemalloc.start()
    before_mem = process.memory_info().rss
    res = binary_divide(arr_m, arr_n)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    after_mem = process.memory_info().rss
    memory_used = max(peak / 1024, after_mem - before_mem)  # kbytes

    start = time.perf_counter()
    for _ in range(NUM_MULTIPLE_LAUCHES):
        binary_divide(arr_m, arr_n)
    time_spent = (time.perf_counter() - start) / NUM_MULTIPLE_LAUCHES

    return res, time_spent, memory_used