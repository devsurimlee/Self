import sys
input = sys.stdin.readline

n = int(input())
MAX = 300
stairs = [0 for _ in range(MAX + 1)]
dp = [0 for _ in range(MAX + 1)]

for i in range(n):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    a = stairs[i] + stairs[i - 1] + dp[i - 3]
    b = stairs[i] + dp[i - 2]
    dp[i] = max(a, b)

print(dp[n - 1])
