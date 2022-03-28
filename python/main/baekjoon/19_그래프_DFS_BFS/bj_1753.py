import heapq
import sys
input = sys.stdin.readline

# x, y = 5, 6
# start = 1
# case = [[5, 1, 1], [1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6]]

x, y = map(int, input().split())
start = int(input())

INF = sys.maxsize
visit = [INF] * (x + 1)
graph = [[] for i in range(x + 1)]

def dijkstra():
    queue = []
    heapq.heappush(queue, [0, start])  # 점수, 시작점
    visit[start] = 0

    while queue:
        disc, node = heapq.heappop(queue)
        if visit[node] < disc:
            continue

        for new_node, new_disc in graph[node]:
            new_disc += disc

            if new_disc < visit[new_node]:
                visit[new_node] = new_disc
                heapq.heappush(queue, [new_disc, new_node])


for _ in range(y):
    # a, b, c = case[_][0], case[_][1], case[_][2]
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

dijkstra()

for v in visit[1:]:
    if v == INF:
        print("INF")
    else:
        print(v)

###########################################

# https://www.acmicpc.net/problem/1753
# 최단경로

# 가중치 방향그래프
# 해당 방향으로만 이동가능.
# 다익스트라 알고리즘
