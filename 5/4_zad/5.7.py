import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()

def heap(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[largest]:
        largest = l
    if r < n and arr[r] < arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, - 1, - 1):
        heap(arr, n, i)
    for i in range(n - 1, 0, - 1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)


f = open('input.txt', 'r')
n = int(f.readline())
s = list(map(int, f.readline().split()))
f.close()
heapsort(s)
f = open('output.txt', 'w')
f.write(' '.join(list(map(str, s))))

end = time.time() - start
print(end)
print('{}'.format(mem))
