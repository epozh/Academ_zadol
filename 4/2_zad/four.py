import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()


def check_brackets(string):
    stack = []  # Используется стек для отслеживания открытых скобок

    for i, char in enumerate(string, start=1):
        if char in '([{':  # Если символ - открывающая скобка
            stack.append((char, i))
        elif char in ')]}':  # Если символ - закрывающая скобка
            if not stack:  # Если стек пустой
                return i
            top_char, _ = stack.pop()  # Извлекаем последнюю открывающую скобку из стека
            if (char == ')' and top_char != '(') or \
                    (char == ']' and top_char != '[') or \
                    (char == '}' and top_char != '{'):
                return i

    if stack:  # Если в стеке остались открытые скобки
        _, index = stack.pop()
        return index

    return -1  # Если все скобки сбалансированы


# Чтение скобок из входного файла
with open("input.txt", "r") as file:
    expression = file.read()

# Проверка правильности расстановки скобок
result = check_brackets(expression)

# Запись результата в выходной файл
with open("output.txt", "w") as file:
    if result == -1:
        file.write("Success.")
    else:
        file.write(str(result))


end = time.time() - start
print(end)
print('{}'.format(mem))
