f=open('input.txt')
n, k = f.readline().split()
ls1 = [int(x) for x in f.readline().split()]
ls2 = [int(x) for x in f.readline().split()]
n = int(n)
k = int(k)

def insertion_sort(new):
   for i in range(1, len(new)): # проходим по массиву, начиная со второго элемента
       item = new[i] # элемент, для которого хотим найти правильную позицию в массиве
       j = i - 1 # элемент, который изначально был впереди элемента
       while j >= 0 and new[j] > item: # если элемент массива соседнего значения, сравниваем его с оставшимися
           new[j + 1] = new[j] # сдвигаем значение на одну позицию влево так, чтобы j указывал на следующий элемент
           j -= 1
       new[j + 1] = item # когда мы закончили сравнение со всеми элементами,помещаем элемент на правильную позицию
   s=0
   for x in range(0, len(new)):
           if x % 10 == 0:
               s += new[x]
   return s
def multiply(ls1, ls2):
   new = []
   for i in ls2:
       for j in ls1:
           a=i*j
           new.append(a)
   return insertion_sort(new)
res = str(multiply(ls1, ls2))
f = open('output.txt', 'w')
f.write(" ".join(map(str, res)))