import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()


class MaxStack:
    def __init__(self):
        self.stack = []  # основной стек
        self.max_stack = []  # стек максимальных значений

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()

    def max(self):
        return self.max_stack[-1]


with open('input.txt', 'r') as fr:
    n = int(fr.readline())
    commands = [fr.readline().strip().split() for _ in range(n)]

stack = MaxStack()
result = []
for command in commands:
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        stack.pop()
    elif command[0] == 'max':
        result.append(str(stack.max()))

with open('output.txt', 'w') as fw:
    fw.write('\n'.join(result))

end = time.time() - start
print(end)
print('{}'.format(mem))
