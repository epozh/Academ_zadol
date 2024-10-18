import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()

def ifheap(arr, n):
    for i in range(1, n // 2 + 1):
        if not arr[i - 1] <= arr[2 * i - 1] or not arr[i - 1] <= arr[2 * i]:
            return False
    return True


with open('input.txt') as f:
   n = int(f.readline())
   arr = [int(i) for i in f.readline().split()]


with open('output.txt', 'w') as f:
    if ifheap(arr, n):
        f.write('YES')
    else:
        f.write('NO')


end = time.time() - start
print(end)
print('{}'.format(mem))