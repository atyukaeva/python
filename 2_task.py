def sort_numbers(lst: list) -> list:
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] > lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst


if __name__ == '__main__':
  print('Введите список чисел любой ненулевой длины через запятую (например: 3,2,1):')
  numbers = list(input().split(","))

  result = sort_numbers(numbers)
  print(result)
    