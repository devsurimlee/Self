# https://www.acmicpc.net/problem/10250

import math

cnt = int(input())

for i in range(cnt):
    h, w, n = map(int, input().split())
    aa = n % h
    bb = math.ceil(n / h)

    # 층수 계산시 0일 경우 case 주의
    if aa == 0:
        aa = h
    if bb < 10:
        bb = '0' + str(bb)

    print(f'{aa}{bb}')

# H W N번째손님
# 2
# 6 12 10
# 30 50 72

##################
# 402
# 1203
