import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()


def stack_operations(commands):
    stack = []
    deleted_elements = []

    for command in commands:
        command = command.strip()
        if command == '-':
            deleted_elements.append(stack.pop())
        else:
            stack.append(int(command.split()[1]))

    return deleted_elements


# считываем число команд
with open('input.txt', 'r') as file:
    m = int(file.readline())

# считываем команды
with open('input.txt', 'r') as file:
    commands = file.readlines()[1:]

deleted_elements = stack_operations(commands)

# выводим изъятые элементы
with open('output.txt', 'w') as file:
    for element in deleted_elements:
        file.write(str(element) + '\n')

end = time.time() - start
print(end)
print('{}'.format(mem))
