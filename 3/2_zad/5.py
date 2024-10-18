f = open('input.txt', "r")
line = f.readline().strip()
if not line:
    raise ValueError("Файл пуст или содержит некорректные данные")
        
citiz = [int(x) for x in line.split(',') if x.strip().isdigit()]

if not citiz:
    raise ValueError("Файл не содержит корректных целых чисел")


def sorted(citiz):
    for i in range(1, len(citiz)):
        for j in range(i, 0, -1):
            if citiz[j] > citiz[j - 1]:
                citiz[j], citiz[j - 1] = citiz[j - 1], citiz[j]
    return citiz


def hIndex(citiz):
    sorted(citiz)
    n = len(citiz) - 1
    i = 0
    while i < n:
        if citiz[n - i] < i:
            break
        else:
            i += 1
    res = i - 1
    return res


y = hIndex(citiz)
f = open('output.txt', 'w')
f.write(str(y))
