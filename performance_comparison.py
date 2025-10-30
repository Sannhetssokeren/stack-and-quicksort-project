import random
import time
from quick_sort import quick_sort
from insertion_sort import insertion_sort
import matplotlib.pyplot as plt

# Функция для измерения времени выполнения с усреднением
def measure_time_average(sort_func, arr, runs=3):
    """
    Измеряет среднее время выполнения функции сортировки.

    :param sort_func: Функция сортировки.
    :param arr: Входной список.
    :param runs: Количество прогонов для усреднения.
    :return: Среднее время выполнения.
    """
    total_time = 0
    for _ in range(runs):
        arr_copy = arr.copy()  # Копируем массив, чтобы не изменять исходный
        start_time = time.perf_counter() # Используем более точный таймер
        sort_func(arr_copy)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    return total_time / runs

# Фиксируем зерно для воспроизводимости
random.seed(777)

# Измерение времени для разных размеров списков
sizes = [10, 100, 1000, 5000]
quick_sort_times = []
insertion_sort_times = []

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]

    # Время выполнения быстрой сортировки
    quick_sort_time = measure_time_average(quick_sort, arr)
    quick_sort_times.append(quick_sort_time)
    print(f"QuickSort, размер {size}: {quick_sort_time:.6f} сек")

    # Время выполнения сортировки вставками
    insertion_sort_time = measure_time_average(insertion_sort, arr)
    insertion_sort_times.append(insertion_sort_time)
    print(f"InsertionSort, размер {size}: {insertion_sort_time:.6f} сек")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, quick_sort_times, label="Быстрая сортировка", marker='o')
plt.plot(sizes, insertion_sort_times, label="Сортировка вставками", marker='x')
plt.xlabel("Размер списка")
plt.ylabel("Среднее время выполнения (секунды)")
plt.title("Сравнение времени выполнения сортировок")
plt.legend()
plt.grid(True)
plt.savefig("sorting_performance_graph.png")  # Сохранение графика в файл
plt.show()

print("График сохранен как sorting_performance_graph.png")