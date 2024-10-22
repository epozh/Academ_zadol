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

x = ([int(i) for i in s.split()])


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
            arr[i + 1] = key
    return arr


result = insertion_sort(x)

write_output('output.txt', result)
execution_time = time.time() - start
print_execution_details(execution_time, mem)