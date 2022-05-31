n, m = map(int, input().split())

memo = []

def dfs():
    if len(memo) == m:
        return print(' '.join(map(str, memo)))

    for i in range(1, n + 1):
        if i not in memo:
            memo.append(i)
            dfs()
            memo.pop()

dfs()


#############
# dfs > 백트래킹
# https://www.acmicpc.net/problem/15649
# N과 M (1) 성공