import math

def min_heapify(A, i, heap_size):
    global c
    global h
    i = i + 1
    _l = 2 * i
    r = 2 * i + 1
    if _l <= heap_size and A[_l - 1] < A[i - 1]:
        smallest = _l
    else:
        smallest = i
    if r <= heap_size and A[r - 1] < A[smallest - 1]:
        smallest = r
    if smallest != i:
        A[i - 1], A[smallest - 1] = A[smallest - 1], A[i - 1]
        c += 1
        h.append(str(i - 1) + ' ' + str(smallest - 1))
        min_heapify(A, smallest - 1, heap_size)


def build_min_heap(A):  # создание неубывающей пирамиды
    heap_size = len(A)
    global c
    for i in range(math.ceil(heap_size // 2), -1, -1):
        min_heapify(A, i, heap_size)
    return c


f = open('input.txt')
n = int(f.readline())
s = f.readline()
arr = ([int(i) for i in s.split()])
h = []
f.close()
f = open('output.txt', 'w')
c = 0
build_min_heap(arr)
f.write(str(c) + '\n')
for line in h:
    f.write(line + '\n')
f.close()
