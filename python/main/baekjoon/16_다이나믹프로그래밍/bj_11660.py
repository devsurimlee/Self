# width, coin = map(int, input().split())

width, coin = 4, 3
dp = [[0] * (width + 1) for i in range(width + 1)]
case = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 3, 4, 5], [0, 3, 4, 5, 6], [0, 4, 5, 6, 7]]

for i in range(1, width + 1):
    # nums = list(map(int, input().split()))
    nums = case[i]
    for j in range(1, width + 1):
        dp[i][j] = nums[j]

for x in range(1):
    # x1, y1, x2, y2 = list(map(int, input().split()))
    sum = 0
    x1, y1, x2, y2 = 2, 2, 3, 4

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum += dp[i][j]

    print(sum)

# https://www.acmicpc.net/problem/11660 / 구간합 구하기 5

# 2 3 4 5
# 3 4 5 6
#
# 2 5 9 14
# 3 7 12 17
#
# 14+17 -5 = 27
