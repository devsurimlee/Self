# https://www.acmicpc.net/problem/1018

# n = 10
# m = 13

# case = [list('BBBBBBBBWBWBW'), list('BBBBBBBBBWBWB'), list('BBBBBBBBWBWBW'), list('BBBBBBBBBWBWB'),
#         list('BBBBBBBBWBWBW'),
#         list('BBBBBBBBBWBWB'), list('BBBBBBBBWBWBW'), list('BBBBBBBBBWBWB'), list('WWWWWWWWWWBWB'),
#         list('WWWWWWWWWWBWB')]

n, m = map(int, input().split())
aa = list('BWBWBWBW')
bb = list('WBWBWBWB')
size = 8
result = 64

isSwitch = True

case = []
for i in range(n):
    case.append(list(input()))


for x in range(m - size + 1):  # 가로시작점
    for y in range(n - size + 1):  # 세로시작점
        sum1 = 0
        sum2 = 0
        for z in range(size):
            row = case[y + z][x:x + size]
            # row 홀수줄일경우
            if z % 2 == 1:
                isSwitch = True
            # row 짝수줄일경우
            else:
                isSwitch = False
            # 한줄씩 확인
            for i in range(size):
                if row[i] != aa[i]:
                    if isSwitch:
                        sum1 += 1
                    else:
                        sum2 += 1
                if row[i] != bb[i]:
                    if isSwitch:
                        sum2 += 1
                    else:
                        sum1 += 1

        Min = min([sum1, sum2])

        if result > Min:
            result = Min

print(result)




##########################################
 # 백준 numpy 지원안함 ㅠㅠ
# import numpy as np
#
# # n, m = map(int, input().split())
# size = 8
# lists = []
# for i in range(n):
#     # lists.append(list(input()))
#     lists.append(case[i])
#
#
# arr = np.array(lists)
#
# aa = list('BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB')
# bb = list('WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW')
#
# result = 64
# for i in range(n - size + 1):  # 10-8 -> 2
#     for j in range(m - size + 1):  # 13-8 -> 5
#         print(i, j)
#         board = arr[i:i + size, j:j + size]
#         row = np.concatenate(board)
#
#         if i == 0 and j == 5:
#             print(row)
#
#         check1 = 0
#         check2 = 0
#
#         for x in range(len(row)):
#             if row[x] != aa[x]:
#                 check1 += 1
#             if row[x] != bb[x]:
#                 check2 += 1
#
#         Min = min([check1, check2])
#
#         if result > Min:
#             result = Min
#         # print(check1, check2)
#
# print(result)

# 0~8:0~8, 1~9:0~8

############################

# 10 13 - > 12
# BBBBBBBBWBWBW 0
# BBBBBBBBBWBWB 1
# BBBBBBBBWBWBW 2
# BBBBBBBBBWBWB 3
# BBBBBBBBWBWBW 4
# BBBBBBBBBWBWB 5
# BBBBBBBBWBWBW 6
# BBBBBBBBBWBWB 7
# WWWWWWWWWWBWB 8
# WWWWWWWWWWBWB 9
