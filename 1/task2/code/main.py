import time
import psutil

from utils import get_memory_usage
from utils import get_current_time
from utils import read_input_file
from utils import write_output
from utils import print_execution_details


x = ([int(i) for i in s.split()])


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and key > arr[i]:
            t = arr[i]
            arr[i] = key
            arr[i + 1] = t
            i = i - 1
    return arr


result = insertion_sort(x)

write_output_and_print_details('output.txt', result, start, mem)

if __name__ == '__main__':
    mem_usage_before = get_memory_usage()
    start_time = get_current_time()
    n, s = read_input_file('input.txt')
