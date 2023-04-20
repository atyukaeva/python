# Натуральное число p является простым, если оно отлично от 1 и делится без остатка только на 1 и на само p
def definition_prime_number(number: int) -> float:
    if number < 2:
        return False

    for num in range(2, number - 1):
        if number % num == 0 and number != num:
            return False

    return True


# Обработчик вводимых данных
def get_input() -> int:
    while True:
        try:
            num = int(input())
            if num < 0 or num > 1000:
                raise Exception("Число больше 1000 или меньше 0")

            return num
        except ValueError as exc:
            print(f"Введеная строка не удовлетворяет условию задачи. Попробуйте заново.\nПодробнее: {exc}")
        except Exception as exc:
            print(f"{exc}\nПопробуйте заново: ")


# Точка входа в программу
if __name__ == '__main__':
    while True:
        print("Введите число (от 0 до 1000): ")
        number = get_input()

        result = definition_prime_number(number)
        print(result)

        print("Для продолжения нажмите Ввод или n - для выхода из программы")
        if input() == "n":
            break
