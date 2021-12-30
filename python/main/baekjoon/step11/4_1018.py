# https://www.acmicpc.net/problem/1018


n = 10
m = 13

case = [list('BBBBBBBBWBWBW'),list('BBBBBBBBBWBWB'),list('BBBBBBBBWBWBW'),list('BBBBBBBBBWBWB'),list('BBBBBBBBWBWBW'),
         list('BBBBBBBBBWBWB'),list('BBBBBBBBWBWBW'),list('BBBBBBBBBWBWB'),list('WWWWWWWWWWBWB'),list('WWWWWWWWWWBWB')]

# aa = list('BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB')
# bb = list('WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW')

aa = list('BWBWBWBW')
bb = list('WBWBWBWB')


##########################################
#  백준 numpy 지원안함 ㅠㅠ
# import numpy as np
#
# n, m = map(int, input().split())
# size = 8
# lists = []
# for i in range(n):
#     lists.append(list(input()))
#
# arr = np.array(lists)
#
# aa = list('BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB')
# bb = list('WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW')
#
# result = 64
# for i in range(n - size + 1):  # 10-8 -> 2
#     for j in range(m - size + 1):  # 13-8 -> 5
#         board = arr[i:i + size, j:j + size]
#         row = np.concatenate(board)
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
