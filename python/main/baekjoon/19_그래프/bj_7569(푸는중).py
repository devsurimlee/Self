import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline

# m, n, h = 5, 3, 1
# m, n, h = 5, 3, 2
# m, n, h = 4, 3, 2
m, n, h = 5, 3, 2
# m, n, h = map(int, input().split())

graph = []
surround = [[1, 0], [-1, -0], [0, 1], [0, -1]]

# case = [[[0, -1, 0, 0, 0], [-1, -1, 0, 1, 1], [0, 0, 0, 1, 1]]] # -1
# case = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]  # 4
# case = [[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, -1]]] # 0
case = [[[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]], [[0, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]]  # 4

for i in range(h):
    li = []
    for j in range(n):
        li.append(case[i][j])
        # li.append(list(map(int, input().split())))
    graph.append(li)


queue = deque([])

for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1:
                queue.append([a, b, c])

print(queue)

dfs()

##########################################

# 시간초과
#
# # 해당요소 값 0일 때만 숫자 할당
# def check_zero(x, y, num):
#     if arr[x][y] == 0:
#         arr[x][y] = num
#
#
# def tomato(v):
#     global before_zero_cnt
#     zero_cnt = 0
#     for i in range(n * h):
#         for j in range(m):
#             if arr[i][j] == v:
#                 for s in surround:
#                     a = i + s[1]
#                     b = j + s[0]
#                     floor = i // n + 1
#                     # 같은 층 체크
#                     if (n * (floor - 1) <= a < n * floor) and (0 <= b < m):
#                         check_zero(a, b, v + 1)
#                 # 윗층 체크
#                 if i - n >= 0:
#                     check_zero(i - n, j, v + 1)
#                 # 아래층 체크
#                 if i + n < n * h:
#                     check_zero(i + n, j, v + 1)
#
#             if arr[i][j] == 0:
#                 zero_cnt += 1
#     if zero_cnt > 0:
#         if before_zero_cnt == zero_cnt:
#             print(-1)
#         else:
#             before_zero_cnt = zero_cnt
#             tomato(v + 1)
#     if zero_cnt == 0:
#         MAX = max(map(max, arr))
#         print(MAX - 1)
#
#
# tomato(1)

# https://www.acmicpc.net/problem/7569
# 토마토 1
