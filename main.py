# imports
from two_pointers import two_pointers_test
from binsec import binary_search_test
from exponential import exponential_search_test
from binary_divide import binary_divide_test

import plotly.graph_objects as go
from plotly.subplots import make_subplots


# short_len = 5_000_000
# long_len = 10_000_000
short_len = 1_000_000
long_len = 10_000_000

# 1) нет пересечения, все элементы m < всех элементов n
#    разная четность, отсортированы, и m[i] < n[i] для любого i
#    m - короткий (5M), n - длинный (10M)
worst_m_1 = [2 * i for i in range(short_len)]  # четные, начинаются с 0
worst_n_1 = [2 * i + 1 for i in range(short_len + 1, long_len + short_len)]  # нечетные, все > max(m)

# 2) m - все четные (короткий), n - все нечетные (длинный)
#    разная четность, отсортированы, и m[i] < n[i] для любого i
worst_m_2 = [2 * i for i in range(short_len)]  # четные, короткий
worst_n_2 = [2 * i + 1 for i in range(long_len)]  # нечетные, длинный
worst_m_2.append(long_len + 4)
worst_n_2.append(long_len + 4)

# 3) m - все нечетные (длинный), n - все четные (короткий)
#    разная четность, отсортированы, и m[i] < n[i] для любого i
worst_m_3 = [2 * i + 1 for i in range(long_len)]  # нечетные, длинный
worst_n_3 = [2 * i + 2 for i in range(short_len)]  # четные, короткий
worst_m_3.append(long_len + 4)
worst_n_3.append(long_len + 4)

# Two pointers
print("start two pointers")
res_two_pointers_1, time_two_pointers_1, mem_two_pointers_1 = two_pointers_test(
    worst_m_1, worst_n_1
)
res_two_pointers_2, time_two_pointers_2, mem_two_pointers_2 = two_pointers_test(
    worst_m_2, worst_n_2
)
res_two_pointers_3, time_two_pointers_3, mem_two_pointers_3 = two_pointers_test(
    worst_m_3, worst_n_3
)

# Binary search
print("start binary search")
res_binary_search_1, time_binary_search_1, mem_binary_search_1 = binary_search_test(
    worst_m_1, worst_n_1
)
res_binary_search_2, time_binary_search_2, mem_binary_search_2 = binary_search_test(
    worst_m_2, worst_n_2
)
res_binary_search_3, time_binary_search_3, mem_binary_search_3 = binary_search_test(
    worst_m_3, worst_n_3
)

# Exponential search
print("start exponential search")
res_exponential_search_1, time_exponential_search_1, mem_exponential_search_1 = exponential_search_test(
    worst_m_1, worst_n_1
)
res_exponential_search_2, time_exponential_search_2, mem_exponential_search_2 = exponential_search_test(
    worst_m_2, worst_n_2
)
res_exponential_search_3, time_exponential_search_3, mem_exponential_search_3 = exponential_search_test(
    worst_m_3, worst_n_3
)

# Binary divide
print("start binary divide")
res_binary_divide_1, time_binary_divide_1, mem_binary_divide_1 = binary_divide_test(
    worst_m_1, worst_n_1
)
res_binary_divide_2, time_binary_divide_2, mem_binary_divide_2 = binary_divide_test(
    worst_m_2, worst_n_2
)
res_binary_divide_3, time_binary_divide_3, mem_binary_divide_3 = binary_divide_test(
    worst_m_3, worst_n_3
)

datasets = ["dataset_1", "dataset_2", "dataset_3"]

# Two Pointers: build chart
print("start chart two pointers")
two_pointers_times = [
    time_two_pointers_1,
    time_two_pointers_2,
    time_two_pointers_3,
]
two_pointers_mems = [
    mem_two_pointers_1,
    mem_two_pointers_2,
    mem_two_pointers_3,
]

fig_two_pointers = go.Figure(
    data=[
        go.Bar(name="Time", x=datasets, y=two_pointers_times),
        go.Bar(name="Memory", x=datasets, y=two_pointers_mems),
    ]
)
fig_two_pointers.update_layout(
    title="Two Pointers: Time and Memory per Dataset",
    barmode="group",
    xaxis_title="Dataset",
    yaxis_title="Value (log scale)",
    yaxis_type="log",
)
fig_two_pointers.write_html("charts/two_pointers_worst_cases.html")

# Binary Search: build chart
print("start chart binary search")
binary_search_times = [
    time_binary_search_1,
    time_binary_search_2,
    time_binary_search_3,
]
binary_search_mems = [
    mem_binary_search_1,
    mem_binary_search_2,
    mem_binary_search_3,
]

fig_binary_search = go.Figure(
    data=[
        go.Bar(name="Time", x=datasets, y=binary_search_times),
        go.Bar(name="Memory", x=datasets, y=binary_search_mems),
    ]
)
fig_binary_search.update_layout(
    title="Binary Search: Time and Memory per Dataset",
    barmode="group",
    xaxis_title="Dataset",
    yaxis_title="Value (log scale)",
    yaxis_type="log",
)
fig_binary_search.write_html("charts/binary_search_worst_cases.html")

# Exponential Search: build chart
print("start chart exponential search")
exponential_search_times = [
    time_exponential_search_1,
    time_exponential_search_2,
    time_exponential_search_3,
]
exponential_search_mems = [
    mem_exponential_search_1,
    mem_exponential_search_2,
    mem_exponential_search_3,
]

fig_exponential_search = go.Figure(
    data=[
        go.Bar(name="Time", x=datasets, y=exponential_search_times),
        go.Bar(name="Memory", x=datasets, y=exponential_search_mems),
    ]
)
fig_exponential_search.update_layout(
    title="Exponential Search: Time and Memory per Dataset",
    barmode="group",
    xaxis_title="Dataset",
    yaxis_title="Value (log scale)",
    yaxis_type="log",
)
fig_exponential_search.write_html("charts/exponential_search_worst_cases.html")

# Binary Divide: build chart
print("start chart binary divide")
binary_divide_times = [
    time_binary_divide_1,
    time_binary_divide_2,
    time_binary_divide_3,
]
binary_divide_mems = [
    mem_binary_divide_1,
    mem_binary_divide_2,
    mem_binary_divide_3,
]

fig_binary_divide = go.Figure(
    data=[
        go.Bar(name="Time", x=datasets, y=binary_divide_times),
        go.Bar(name="Memory", x=datasets, y=binary_divide_mems),
    ]
)
fig_binary_divide.update_layout(
    title="Binary Divide: Time and Memory per Dataset",
    barmode="group",
    xaxis_title="Dataset",
    yaxis_title="Value (log scale)",
    yaxis_type="log",
)
fig_binary_divide.write_html("charts/binary_divide_worst_cases.html")

