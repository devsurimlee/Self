n, m = map(int, input().split())
memo = []


def dfs():
    if len(memo) == m:
        return print(' '.join(map(str, memo)))

    for i in range(1, n + 1):
        memo.append(i)
        dfs()
        memo.pop()


dfs()

########################

# https://www.acmicpc.net/problem/15651
# N과 M (3) / 백트래킹
