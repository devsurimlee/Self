n, m = map(int, input().split())
num_list = sorted(map(int, input().split()))
memo = []


def dfs():
    if len(memo) == m:
        return print(' '.join(map(str, memo)))

    for num in sorted(set(num_list)):
        if len(memo) == 0 or num_list.count(num) > memo.count(num):
            memo.append(num)
            dfs()
            memo.pop()

dfs()

#######################################
# https://www.acmicpc.net/problem/15663
# N과 M (9) / 백트래킹
