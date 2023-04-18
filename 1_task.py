def definition_prime_number(number: int) -> float:
    if number < 2:
        return False

    for num in range(2, number - 1):
        if number % num == 0 and number != num:
            return False

    return True

if __name__ == '__main__':
    print("Введите число (от 0 до 1000): ")
    number = int(input())

    result = definition_prime_number(number)
    print(result)
