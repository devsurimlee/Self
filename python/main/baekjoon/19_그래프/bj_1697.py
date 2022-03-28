from collections import deque


def bfs():
    queue = deque([n])
    while queue:
        x = queue.popleft()

        if x == k:
            print(visit_list[x])
            exit(0)

        cals = [x - 1, x + 1, x * 2]
        for c in cals:
            if 0 <= c <= limit and visit_list[c] == 0:
                visit_list[c] = visit_list[x] + 1
                queue.append(c)


n, k = map(int, input().split())
limit = 10 ** 5
visit_list = [0 for i in range(limit + 1)]

bfs()

# https://www.acmicpc.net/problem/1697
# 숨바꼭질1
