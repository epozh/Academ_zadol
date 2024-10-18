import time
import psutil

mem = psutil.Process().memory_info().rss
start = time.time()

def longest_common_subsequence_length(A, B, C):
    m = len(A)
    n = len(B)
    l = len(C)

    dp = [[[0 for _ in range(l+1)] for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(1, l+1):
                if A[i-1] == B[j-1] and A[i-1] == C[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[m][n][l]

with open("input.txt", "r") as file:
    n = int(file.readline())
    A = list(map(int, file.readline().split()))
    m = int(file.readline())
    B = list(map(int, file.readline().split()))
    l = int(file.readline())
    C = list(map(int, file.readline().split()))

result = longest_common_subsequence_length(A, B, C)

with open("output.txt", "w") as file:
    file.write(str(result))

end = time.time() - start
print(end)
print('{}'.format(mem))
