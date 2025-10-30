def fibonacci_with_trace(n, depth=0):
    """
    Вычисляет n-е число Фибоначчи рекурсивно с трассировкой стека вызовов.

    :param n: Номер числа Фибоначчи.
    :param depth: Глубина рекурсии (для отступов в трассировке).
    :return: n-е число Фибоначчи.
    """
    indent = "  " * depth
    print(f"{indent}Вызов fibonacci({n})")

    if n <= 0:
        print(f"{indent}Возврат 0 (n <= 0)")
        return 0
    if n == 1 or n == 2:  # Базовый случай
        print(f"{indent}Возврат 1 (n == 1 или n == 2)")
        return 1

    result = fibonacci_with_trace(n - 1, depth + 1) + fibonacci_with_trace(n - 2, depth + 1)
    print(f"{indent}Возврат {result} для fibonacci({n})")
    return result

# Анализ стека вызовов для n = 5
if __name__ == "__main__":
    n = 5
    print(f"--- Анализ стека вызовов для fibonacci({n}) ---")
    result = fibonacci_with_trace(n)
    print(f"--- Результат: {result} ---")