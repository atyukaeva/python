# Поиск скобок
def searching_brackets(string: str) -> str:
    while True: 
        open = string.find("(")
        close = string.find(")")

        if open > -1 and close > -1: 
            string = string[0:open] + string[close+1:len(string)]
        else:
            return string


# Точка входа в программу
if __name__ == '__main__':
  print('Введите текст:')
  string = input()

  result = searching_brackets(string)

  print(f"Результат: {result}")
    