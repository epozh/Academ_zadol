import time
import psutil
mem = psutil.Process().memory_info().rss
start = time.time()

f = open('input.txt', 'r')
n = int(f.readline())
s = f.readline()
f.close()

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

f = open('output.txt', 'w')
f.write(' '.join(map(str, result)))
f.close()

end = time.time() - start
print(end)
print('{}'.format(mem))
