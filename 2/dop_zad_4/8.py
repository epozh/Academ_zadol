f = open('input.txt', 'r')

n = int(f.readline())
a = list(map(int, f.readline().split()))
b = list(map(int, f.readline().split()))

res = [0]*(n+2)
for i in range(n):
   for j in range(n):
       res[i+j]+=(a[i]*b[j])

f = open('output.txt', 'w')

f.write(' '.join(list(map(str, res))))