def test_interpreter():
    # Тестирование вывода на экран
    print("Привет, это тест интерпретатора Python!")

    # Тестирование переменных и операций
    x = 5
    y = 3
    sum_result = x + y
    print(f"Сложение: {x} + {y} = {sum_result}")

    # Тестирование условного оператора
    if x > y:
        print(f"{x} больше, чем {y}")
    elif x < y:
        print(f"{x} меньше, чем {y}")
    else:
        print(f"{x} равно {y}")

    # Тестирование цикла
    for i in range(3):
        print(f"Это итерация номер {i + 1}")

    # Тестирование функции
    def square(num):
        return num ** 2

    result = square(x)
    print(f"Квадрат числа {x}: {result}")

    # Тестирование списка
    numbers = [1, 2, 3, 4, 5]
    print("Это наш список чисел:", numbers)

    # Тестирование обработки исключений
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Ошибка деления на ноль!")


if __name__ == "__main__":
    test_interpreter()
