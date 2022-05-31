n, m = map(int, input().split())
memo = []

def dfs():
    if len(memo) == m:
        print(' '.join(map(str, memo)))

    for i in range(1, n + 1):
        if len(memo) == 0 or i > memo[-1]:   # <- 오름차순으로 증가하므로 마지막 원소보다 크면 넣는걸로 함
            memo.append(i)
            dfs()
            memo.pop()


dfs()

################
# 이전코드

n, m = map(int, input().split())

memo = []
sets = []


def dfs():
    if len(memo) == m:
        if len(sets) > 0:
            for s in sets:
                if s == set(memo):
                    return
        print(' '.join(map(str, memo)))
        sets.append(set(memo))
        return

    for i in range(1, n + 1):
        if i not in memo:
            memo.append(i)
            dfs()
            memo.pop()


dfs()


# dfs > 백트래킹
# https://www.acmicpc.net/problem/15650
# N과 M (2) 성공