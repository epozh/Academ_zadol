import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()

with open("input.txt") as f:
    lines = f.readlines()

votes = {}
for line in lines:
    candidate, count = line.strip().split(" ")
    count = int(count)
    if candidate in votes:
        votes[candidate] += count
    else:
        votes[candidate] = count

with open("output.txt", "w") as file:
    for candidate in sorted(votes.keys()):
        count = votes[candidate]
        file.write(f"{candidate} {count}\n")

end = time.time() - start
print(end)
print('{}'.format(mem))
