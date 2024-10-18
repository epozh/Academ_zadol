def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A,p,q,r)
    return A

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    i, j = 0, 0
    k = p
    while i < len(L) and j < len(R) and k <= r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1
        if i < len(L):
            while i < len(L) and k <= r:
                A[k] = L[i]
                i = i + 1
                k = k + 1
        if j < len(R):
            while j < len(L) and k <= r:
                A[k] = R[j]
                j = j + 1
                k = k + 1
        f.write(str(p + 1) + " ")
        f.write(str(r + 1) + " ")
        f.write(str(A[p]) + " ")
        f.write(str(A[r]) + " ")
        f.write("\n")

with open('input.txt') as f:
    n = int(f.readline())
    stroka = f.readline()
stroka = stroka.split()
spisok = []
for i in stroka:
    spisok.append(int(i))

f = open("output.txt", "w")
merge_sort(spisok, 0, len(spisok) - 1)
for i in spisok:
    f.write(str(i) + " ")
f.close()