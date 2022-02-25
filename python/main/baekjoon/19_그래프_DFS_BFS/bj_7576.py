import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

# m, n = 6, 4
m, n = map(int, input().split())

# case = [[0, -1, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
graph = []
point = [[1, 0], [-1, 0], [0, 1], [0, -1]]

queue = deque([])

for _ in range(n):
    graph.append(list(map(int, input().split())))
    # graph.append(case[_])


def bfs():
    while queue:
        x, y = queue.popleft()

        for p in point:
            a = x + p[0]
            b = y + p[1]

            if 0 <= a < n and 0 <= b < m and graph[a][b] == 0:
                graph[a][b] = graph[x][y] + 1
                queue.append([a, b])


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)     # 완전종료

print(max(map(max, graph)) - 1)



###################

# https://www.acmicpc.net/problem/7576
# 토마토2 / 2차원배열
