import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()

def fibbonachi(el):
    a,b = 0,1
    while a < el:
        a, b = b, a+b
    if a == el or b == el:
        return True
    return False

with open('input.txt') as f:
    _ = int(f.readline())
    digits = list(map(int, f.readlines()))
answer = []
for element in digits:
    if fibbonachi(element):
        answer.append("Yes")
    else:
        answer.append("No")

with open('output.txt', "w") as f:
    f.write("\n".join(answer))

end = time.time() - start
print(end)
print('{}'.format(mem))
