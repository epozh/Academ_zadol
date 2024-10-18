import time
import psutil
mem = psutil.Process().memory_info().rss
start = time.time()

f = open('input.txt')
n = int(f.readline())
a = [0, 1]
for i in range(n - 1):
    a.append((a[i] + a[i + 1]) % 10)
f = open('output.txt', 'w')
f.write(str(a[n]))
f.close()

end = time.time() - start
print('{}'.format(mem))
print(end)