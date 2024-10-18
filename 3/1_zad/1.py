from random import randint

f = open("input.txt", "r")
line = f.readline().strip()
if not line.isdigit():
    raise ValueError("Первая строка не содержит целое число")

n = int(line)

s = f.readline().strip()
arr = [int(x) for x in s.split() if x.isdigit()] 

def quicksort(arr):
   if len(arr) <= 1:
       return arr
   else:
       q = arr[randint(0, len(arr) - 1)]
   l_arr = [n for n in arr if n < q]
   e_arr = [q] * arr.count(q)
   b_arr = [n for n in arr if n > q]
   return quicksort(l_arr) + e_arr + quicksort(b_arr)

f = open('output.txt', 'w')
f.write(' '.join(map(str, quicksort(arr))))