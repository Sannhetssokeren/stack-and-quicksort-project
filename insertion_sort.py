def insertion_sort(arr):
    """
    Сортирует список методом сортировки вставками (Insertion Sort).

    :param arr: Список для сортировки.
    :return: Новый отсортированный список.
    """
    # ВАЖНО: Это "функциональная" реализация, которая НЕ in-place.
    # Она создает новый список и вставляет элементы в нужные позиции.
    # Сложность в среднем и худшем случае: O(n^2), в лучшем: O(n).

    sorted_arr = []
    for element in arr:
        # Найти правильную позицию для вставки элемента
        pos = 0
        while pos < len(sorted_arr) and sorted_arr[pos] < element:
            pos += 1
        sorted_arr.insert(pos, element)
    return sorted_arr

# Пример использования (необязательно для сравнения)
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"Отсортированный список (вставками): {insertion_sort(arr)}")