import math

def max_heapify(A, i):
    i = i + 1
    _l = 2 * i
    r = 2 * i + 1
    if _l <= len(A) and A[_l - 1] > A[i - 1]:
        largest = _l
    else:
        largest = i
    if r <= len(A) and A[r - 1] > A[largest - 1]:
        largest = r
        if largest != i:
            A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
            max_heapify(A, largest - 1)


def build_max_heap(A):
    for i in range(math.ceil(len(A) // 2), -1, -1):
        max_heapify(A, i)


def min_heapify(A, i):
    i = i + 1
    _l = 2 * i
    r = 2 * i + 1
    if _l <= len(A) and A[_l - 1] < A[i - 1]:
        smallest = _l
    else:
        smallest = i
    if r <= len(A) and A[r - 1] < A[smallest - 1]:
        smallest = r
    if smallest != i:
        A[i - 1], A[smallest - 1] = A[smallest - 1], A[i - 1]
        min_heapify(A, smallest - 1)


def build_min_heap(A):
    for i in range(math.ceil(len(A) // 2), -1, -1):
        min_heapify(A, i)


def heap_increase_key(A, i, key):
    i = i + 1
    parent = math.ceil(i // 2)
    A[i - 1] = key
    while i > 1 and A[parent - 1] < A[i - 1]:
        A[i - 1], A[parent - 1] = (A[parent - 1], A[i - 1])
        i = parent


def heap_insert(A, key):
    A.append(None)
    heap_increase_key(A, len(A) - 1, key)


def heap_extract_min(A):
    if len(A) < 1:
        return '*'
    build_min_heap(A)
    min = A[0]
    A.pop(0)
    build_max_heap(A)
    return min


def heap_decrease_key(A, i, key):
    A[i] = key
    max_heapify(A, i)

f_i = open('input.txt')
n = int(f_i.readline())
f_o = open('output.txt', 'w')
A = list()
for j in range(n):
    S = list(f_i.readline().split())
    if S[0] == 'A':
        heap_insert(A, int(S[1]))
    if S[0] == 'X':
        f_o.write(str(heap_extract_min(A)))
        f_o.write('''
''')
    if S[0] == 'D':
        f_i.seek(0)
        S_D = list(f_i.readlines()[int(S[1])].split())
        S_D[1] = int(S_D[1])
        i = A.index(S_D[1])
        heap_decrease_key(A, i, int(S[2]))
        f_i.seek(0)
        for k in range(j + 2):
            f_i.readline()
f_i.close()
f_o.close()
