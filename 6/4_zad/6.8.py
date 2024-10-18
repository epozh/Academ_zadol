class HashTable:
   def __init__(self):
       self.table = set()

   def add_key(self, key):
       self.table.add(key)

   def check_key(self, key):
       if key in self.table:
           return True
       return False

with open('input.txt', 'r', encoding='utf-8') as file_input, \
       open('output.txt', 'w', encoding='utf-8') as file_output:

   N, X, A, B = map(int, file_input.readline().split())
   AC, BC, AD, BD = map(int, file_input.readline().split())

   hash_table = HashTable()

   for _ in range(N):
       if hash_table.check_key(X):
           A = (A + AC) % 10**3
           B = (B + BC) % 10**15
       else:
           hash_table.add_key(X)
           A = (A + AD) % 10**3
           B = (B + BD) % 10**15

       X = (X * A + B) % 10**15

   print(X, A, B, file=file_output)