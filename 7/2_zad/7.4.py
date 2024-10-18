import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()

def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

with open('input.txt') as f:
    n = int(f.readline())
    A = [int(i) for i in f.readline().split()]
    m = int(f.readline())
    B = [int(i) for i in f.readline().split()]

p = longest_common_subsequence(A,B)

with open('output.txt', 'w') as f:
    f.write(str(int(p)))

end = time.time() - start
print(end)
print('{}'.format(mem))

