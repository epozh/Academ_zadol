import time
import psutil

def get_memory_usage():
    return psutil.Process().memory_info().rss

def read_input_file(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        s = f.readline().strip()
    return n, s

def read_input_file(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        s = f.readline().strip()  # Убираем возможные пробелы в конце строки
    return n, s

def write_output(filename, result):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, result)))

def print_execution_details(execution_time, memory_usage):
    print(f"Время выполнения: {execution_time:.4f} секунд")
    print(f"Использование памяти: {memory_usage} байт")

