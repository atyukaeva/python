# Сортировка по возрастанию
def sort_numbers(lst: list) -> list:
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] > lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst
    
# Обработчик вводимых данных
def get_input() -> float:
    while True:
        try:
            return list(map(float, input().split(",")))
        except ValueError as exc:
            print(f"Введеная строка не удовлетворяет условию задачи. Попробуйте заново.\nПодробнее: {exc}")


# Точка входа в программу
if __name__ == '__main__':
    while True:
        print('Введите список чисел любой ненулевой длины через запятую (например: 3,2,1):')
        numbers = get_input()

        result = sort_numbers(numbers)
        print()
        print(f"Результат сортировки: {', '.join(map(str, result))}")

        print("Для продолжения нажмите Ввод или n - для выхода из программы")
        if input() == "n":
            break
    