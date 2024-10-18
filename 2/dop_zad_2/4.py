def Binary_search(A, low, high, V):
    if high < low:
        return -1
    mid = low + (high - low) // 2
    if V == A[mid]:
        return mid
    elif V < A[mid]:
        return Binary_search(A, low, mid - 1, V)
    else:
        return Binary_search(A, mid + 1, high, V)

with open('input.txt') as f:
    n = int(f.readline())
    a = f.readline().split()
    k = int(f.readline())
    b = f.readline().split()
spisok = []
for i in a:
    spisok.append(int(i))
find = []
for i in b:
    find.append(int(i))
itog = []
for j in find:
    itog.append(Binary_search(spisok,0,len(spisok)-1,j))
f = open("output.txt","w")
for i in itog:
    f.write(str(i) + " ")
f. close()