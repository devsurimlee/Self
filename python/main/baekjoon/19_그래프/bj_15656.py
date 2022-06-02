n, m = map(int, input().split())
num_list = sorted(map(int, input().split()))
memo = []


def dfs():
    if len(memo) == m:
        return print(' '.join(map(str, memo)))

    for num in num_list:
        memo.append(num)
        dfs()
        memo.pop()


dfs()

#######################################
# https://www.acmicpc.net/problem/15656
# N과 M (7) / 백트래킹
