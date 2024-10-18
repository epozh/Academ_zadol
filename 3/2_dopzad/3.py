def is_sorted(arr):
  for i in range(1, len(arr)):
   if int(arr[i]) < int(arr[i - 1]):
     return False
  return True

def scarecrow_sort(arr, k):
  for i in range(len(arr) - k):
   if int(arr[i]) > int(arr[i + k]):
     arr[i], arr[i + k] = arr[i + k], arr[i]

  return 'Yes' if is_sorted(arr) else 'No'


f = open('input.txt')
a = f.readline().split()
for i in range(len(a)):
  n = int(a[0])
  k = int(a[1])
arr = f.readline().split()
f.close()
f1 = open('output.txt', 'w')
f1.write(scarecrow_sort(arr,k))
f1.close()