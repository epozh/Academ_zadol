import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()


def biggest_subs(a):
    subs = [[] for i in range(len(a))]
    biggest_subs = [a[0]]
    for i in range(len(a)):
        for j in range(i):
            if a[i] > a[j] and len(subs[j]) > len(subs[i]):
                subs[i] = subs[j].copy()
        subs[i].append(seq[i])
        if len(subs[i]) > len(biggest_subs):
            biggest_subs = subs[i]
    return biggest_subs


with open('input.txt', 'r') as f:
    _ = int(f.readline())
    seq = list(map(int, f.readline().split()))
    bis = biggest_subs(seq)
with open('output.txt', 'w') as f:
    f.write(str(len(bis)) + '\n' + ' '.join(map(str, bis)))

end = time.time() - start
print(end)
print('{}'.format(mem))
