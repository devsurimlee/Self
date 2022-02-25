import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# n, m = 5, 5
# case = [[1, 3], [1, 4], [4, 5], [4, 3], [3, 2]]
graph = [[0 for i in range(n + 1)] for i in range(n + 1)]

each_score = []
rank_score = [0 for i in range(n + 1)]
queue = deque([])

def bfs(people):
    each_score = [0 for i in range(n + 1)]
    while queue:
        v = queue.popleft()
        for i in range(1, n + 1):
            if graph[v][i] == 1 and each_score[i] == 0:
                each_score[i] = each_score[v] + 1
                queue.append(i)

    each_score[people] = 0
    rank_score[people] = sum(each_score)


for i in range(m):
    a, b = map(int, input().split())
    # a, b = case[i][0], case[i][1]
    graph[a][b] = graph[b][a] = 1

for people in range(1, n + 1):
    queue.append(people)
    bfs(people)

min_score = min(rank_score[1:-1])
print(rank_score.index(min_score))


###################################

# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙

# bfs 이용하여 단계 넘어갈경우 1점 추가하도록 함
