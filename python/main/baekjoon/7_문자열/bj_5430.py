import sys

input = sys.stdin.readline

t = int(input())
R = 'R'
D = 'D'
error = 'error'

for _ in range(t):
    order = list(input().replace('RR', ''))
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')

    if order.count(D) > n:
        print(error)
    else:
        r_cnt = 0
        odd_cnt = 0
        even_cnt = 0
        for i in order:
            if i == R:
                r_cnt += 1
            elif i == D:
                if r_cnt % 2 == 1:  # R이 홀수
                    odd_cnt += 1
                elif r_cnt % 2 == 0:  # R이 짝수
                    even_cnt += 1

        # R이 짝수일땐 왼쪽에서 절삭, R이 홀수일땐 오른쪽에서 절삭이므로 배열을 마지막에 자름
        arr = arr[even_cnt:n - odd_cnt]
        if r_cnt % 2 == 1:
            print('[' + ','.join(arr[::-1]) + ']')
        else:
            print('[' + ','.join(arr) + ']')


# 41308 kb	180 ms

##############################

# 기존코드  	120668 kb	1736 ms

# import ast
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# t = int(input())
# R = 'R'
# D = 'D'
# error = 'error'
#
# for _ in range(t):
#     order = list(input().rstrip().replace('RR', ''))
#     n = int(input())
#     arr = deque(ast.literal_eval(input()))
#
#     if order.count(D) > n:
#         print(error)
#     else:
#         cnt = 0
#         for i in range(len(order)):
#             if order[i] == R:
#                 cnt += 1
#             elif order[i] == D:
#                 if cnt % 2 == 1:  # 이전에 R이 홀수였음
#                     arr.pop()
#                 elif cnt % 2 == 0:
#                     arr.popleft()
#
#         if order.count(R) % 2 == 1:
#             arr.reverse()
#         print(str(list(arr)).replace(' ', ''))


# https://www.acmicpc.net/problem/5430
# AC
