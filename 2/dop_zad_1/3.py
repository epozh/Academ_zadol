inv_count = 0
def merge_sort(A):
    global inv_count
    if len(A) < 2:
        return A
    else:
        q = len(A) // 2
        L = merge_sort(A[:q])
        R = merge_sort(A[q:])
        sorted_A = merge(L, R)
        return sorted_A

def merge(L, R):
    global inv_count
    result = []
    i, j = 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            inv_count += len(L) - i
            j += 1
    if i < len(L):
        result += L[i:]
    if j < len(R):
        result += R[j:]
    return result


with open('input.txt') as f:
    n = int(f.readline())
    stroka = f.readline()
stroka = stroka.split()
spisok = []
for i in stroka:
    spisok.append(int(i))
f = open("output.txt","w")
merge_sort(spisok)
f.write(str(inv_count))