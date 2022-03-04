import sys
from collections import deque

input = sys.stdin.readline

# n = 7
n = int(input())
# case = ['1 6', '6 3', '3 5', '4 1', '2 4', '4 7']
graph = [[] for _ in range(n + 1)]
visit_list = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    # a, b = map(int, case[_].split())

    graph[a].append(b)
    graph[b].append(a)


def bfs():
    queue = deque([1])
    visit_list[1] = 1
    while queue:
        x = queue.popleft()

        for i in range(len(graph[x])):
            target = graph[x][i]
            if visit_list[target] == 0:
                queue.append(target)
                visit_list[target] = x

    for i in range(2, n + 1):
        print(visit_list[i])


bfs()

#########################################
# 기존에 쓰는 것처럼 n * n 배열로 생성하니 n 최대값이 10만이라 메모리초과남
# 노드에 연결된 값만 넣고 index 사용하여 해결.

#
# https://www.acmicpc.net/problem/11725
# 트리의 부모찾기

#        1
#    6       4
#    3     2   7
#    5
