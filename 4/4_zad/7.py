import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()


with open("input.txt", "r") as input_file:
    n = int(input_file.readline())
    numbers = list(map(int, input_file.readline().split()))
    m = int(input_file.readline())

with open("output.txt", "w") as output_file:
    left = 0
    right = m - 1
    max_window = max(numbers[left:right + 1])
    output_file.write(str(max_window) + " ")

    while right < n - 1:
        left += 1
        right += 1

        if numbers[right] > max_window:
            max_window = numbers[right]
        elif numbers[left - 1] == max_window:
            max_window = max(numbers[left:right + 1])
        output_file.write(str(max_window) + " ")


end = time.time() - start
print(end)
print('{}'.format(mem))
