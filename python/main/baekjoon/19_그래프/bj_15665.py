n, m = map(int, input().split())
num_list = sorted(map(int, input().split()))
memo = []


def dfs():
    if len(memo) == m:
        return print(' '.join(map(str, memo)))

    for num in sorted(set(num_list)):
        memo.append(num)
        dfs()
        memo.pop()


dfs()

#######################################
# https://www.acmicpc.net/problem/15665
# N과 M (11) / 백트래킹
