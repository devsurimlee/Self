import sys

input = sys.stdin.readline

# n = int(input())
# m = int(input())
# n = 7
# m = 6
# case = [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]

n = 3
m = 2
case = [[1, 3], [2, 3]]
arr = [[0 for i in range(n + 1)] for i in range(n + 1)]

cnt = set()
def dfs(start):
    global cnt
    for i in range(1, n + 1):
        if arr[start][i] == 1:
            arr[start][i] = 0
            print(start, i)
            dfs(i)


for i in range(m):
    # a, b = map(int, input().split())
    a, b = case[i][0], case[i][1]       # 테스트용
    arr[a][b] = 1

dfs(1) # 1부터 시작
print(len(cnt) - 1)




# https://www.acmicpc.net/problem/2606 / 바이러스

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
