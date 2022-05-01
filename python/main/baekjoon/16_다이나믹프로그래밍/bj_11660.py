import sys

input = sys.stdin.readline
width, coin = map(int, input().split())

dp = [list(map(int, input().split())) for _ in range(width)]

for i in range(width):
    for j in range(width):
        if j == 0:
            continue
        dp[i][j] += dp[i][j - 1]

for _ in range(coin):
    x1, y1, x2, y2 = list(map(int, input().split()))
    sum = 0

    for z in range(x1 - 1, x2):
        sum += dp[z][y2 - 1]
        if y1 != 1:
            sum -= dp[z][y1 - 2]

    print(sum)

# https://www.acmicpc.net/problem/11660 / 구간합 구하기 5

# 2 3 4 5
# 3 4 5 6
#
# 2 5 9 14
# 3 7 12 17
#
# 14+17 -5 = 27
