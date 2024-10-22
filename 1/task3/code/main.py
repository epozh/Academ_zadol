import time
import psutil
from utils import get_memory_usage
from utils import get_current_time
from utils import read_input_file
from utils import write_output
from utils import print_execution_details

mem_usage_before = get_memory_usage()
start_time = get_current_time()
n, s = read_input_file('input.txt')


def search(n):
    b = []  # пустой массив
    x = len(n)
    for i in range(x):  # проходимся по всем элементам массива
        if n[i] == V:  # если элемент равен p
            b.append(i)  # то закидываем элемент в массив
    if len(b) > 0:
        return len(b), b  # возвращает длина массива и сам массив, если массив b не пустой стал
    elif len(b) == 0:  # массив пустой, значит просто выносится -1
        return '-1'


write_output('output.txt', result)
execution_time = time.time() - start
print_execution_details(execution_time, mem)
