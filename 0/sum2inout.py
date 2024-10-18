import time
start = time.time()

f = open('input.txt', 'r')
s = f.read()
a, b = map(int, s.split())
summa = str(a + b**2)

f = open('output.txt', 'w')
f.write(summa)
f.close()

end = time.time() - start
print(end)