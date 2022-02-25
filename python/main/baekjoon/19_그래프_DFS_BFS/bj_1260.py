import sys

input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
graph = []
for i in range(m):
    a, b = map(int, input().split())
    graph.append([a, b])

# testCode
# n, m, v = 4, 5, 1
# graph = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]

# n, m, v = 5, 5, 3
# graph = [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]]


result = [0] * (n + 1)
arr = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = graph[i][0], graph[i][1]
    arr[a][b] = arr[b][a] = 1

# 깊이우선
def dfs(v):
    result[v] = 1
    print(v, end=' ')

    for i in range(1, n + 1):
        if result[i] == 0 and arr[v][i] == 1:
            dfs(i)

# 너비우선
def bfs(v):
    # queue = deque([v])     # deque쓰는거보다 list가 성능 좋았음
    queue = [v]
    result[v] = 0

    while queue:
        # v = queue.popleft()
        v = queue.pop(0)
        print(v, end=' ')

        for i in range(1, n + 1):
            if result[i] == 1 and arr[v][i] == 1:
                queue.append(i)
                result[i] = 0

dfs(v)
print()
bfs(v)


# https://www.acmicpc.net/problem/1260 // DFS와 BFS

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
#
# 예제 입력 1
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1
# 1 2 4 3
# 1 2 3 4
