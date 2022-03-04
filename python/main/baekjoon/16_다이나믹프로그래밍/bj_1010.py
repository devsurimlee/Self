t = int(input())
MAX = 30
dp = [[0] * MAX for _ in range(MAX)]

for r in range(MAX):
    for n in range(MAX):
        if r == 1:
            dp[r][n] = n
        elif r == n:
            dp[r][n] = 1
        else:
            result1 = 1
            result2 = 1
            result3 = 1

            for x in range(n, 0, -1):
                result1 *= x

            for y in range(n - r, 0, -1):
                result2 *= y

            for z in range(r, 0, -1):
                result3 *= z

            dp[r][n] = result1 // (result2 * result3)

            # nCr = n-1Cr-1 + n-1Cr
            # if n > r:
            #     dp[r][n] = dp[r - 1][n - 1] + dp[r][n - 1]


for i in range(t):
    r, n = map(int, input().split())
    print(dp[r][n])



###############################
# 일반적 방법

# for i in range(t):
#     r, n = map(int, input().split())  # 2 3
#
#     if r == n:
#         print(1)
#     else:
#         result1 = 1
#         result2 = 1
#         result3 = 1
#
#         for i in range(n, 0, -1):
#             result1 *= i
#
#         for j in range(n-r, 0, -1):
#             result2 *= j
#
#         for v in range(r, 0, -1):
#             result3 *= v
#
#         print(result1 // (result2 * result3))

########################

# 경우의 수 계산
# nCr = n!/(n-r)!r!
# nCr = n-1Cr-1 + n-1Cr <- 아니 어떻게 식 세우는거죠 ㅠㅠ



# https://www.acmicpc.net/problem/1010
# 다리 놓기
