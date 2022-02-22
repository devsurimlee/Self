import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

# 깊이우선탐색
def dfs(v):
    global test
    points[v] = 1
    for i in range(1, N + 1):
        if arr[v][i] == 1 and points[i] == 0:
            # arr[v][i] = arr[i][v] = 0
            dfs(i)

N, M = map(int, input().split())
# N, M = 6, 5
# case = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]

# N, M = 6, 8
# case = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6], [5, 4], [2, 4], [2, 3]]

points = [0 for _ in range(N + 1)]
points[0] = 1
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for x in range(M):
    a, b = map(int, input().split())
    # a, b = case[x][0], case[x][1]
    arr[a][b] = arr[b][a] = 1

cnt = 0
while points.count(0) > 0:
    idx = points.index(0)
    dfs(idx)
    cnt += 1

print(cnt)

# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수
