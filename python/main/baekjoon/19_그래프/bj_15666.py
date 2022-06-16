n, m = map(int, input().split())
num_list = sorted(map(int, input().split()))
memo = []


def dfs():
    if len(memo) == m:
        return print(' '.join(map(str, memo)))

    for num in sorted(set(num_list)):
        if len(memo) == 0 or num >= memo[-1]:
            memo.append(num)
            dfs()
            memo.pop()


dfs()

#######################################
# https://www.acmicpc.net/problem/15666
# N과 M (12) / 백트래킹
