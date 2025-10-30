def find_max_recursive(lst, start=0, end=None):
    """
    Находит максимальный элемент в списке с использованием подхода "Разделяй и властвуй".

    :param lst: Список чисел.
    :param start: Начальный индекс подсписка.
    :param end: Конечный индекс подсписка (не включительно).
    :return: Максимальный элемент в подсписке lst[start:end].
    :raises ValueError: Если список пуст.
    """
    if end is None:
        end = len(lst)
    if not lst:
        raise ValueError("Список пуст, невозможно найти максимальный элемент.")

    if start >= end:
        # Это условие не должно сработать при корректных start, end
        raise ValueError("Некорректные индексы.")
    if start == end - 1:  # Базовый случай: один элемент
        return lst[start]

    mid = (start + end) // 2
    left_max = find_max_recursive(lst, start, mid)      # Рекурсивно находим максимум в левой части
    right_max = find_max_recursive(lst, mid, end)      # Рекурсивно находим максимум в правой части

    return max(left_max, right_max)

def find_max(lst):
    """
    Находит максимальный элемент в списке.

    :param lst: Список чисел.
    :return: Максимальный элемент в списке.
    :raises ValueError: Если список пуст.
    """
    return find_max_recursive(lst)

# Пример использования
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"Максимальный элемент: {find_max(arr)}")

    empty_arr = []
    try:
        print(f"Максимальный элемент в пустом списке: {find_max(empty_arr)}")
    except ValueError as e:
        print(f"Ошибка: {e}")