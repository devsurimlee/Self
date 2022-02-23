import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

# m, n, h = 5, 3, 1
m, n, h = 5, 3, 2
# m, n, h = 4, 3, 2
# m, n, h = map(int, input().split())

arr = []
points = [[1, 0], [-1, -0], [0, 1], [0, -1], [0, -n], [0, n]]
# case = [[0, -1, 0, 0, 0], [-1, -1, 0, 1, 1], [0, 0, 0, 1, 1]] # -1
case = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]  # 4
# case = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, -1]] # 0

for i in range(n * h):
    # arr.append(list(map(int, input().split())))
    arr.append(case[i])

before_zero_cnt = 0

def tomato(v):
    global before_zero_cnt
    zero_cnt = 0
    for i in range(n * h):
        for j in range(m):
            if arr[i][j] == v:
                for p in points:
                    try:
                        if arr[i + p[1]][j + p[0]] == 0:
                            if i % n == 0 and p[1] == -1:
                                continue
                            if i % n == 2 and p[1] == 1:
                                continue
                            arr[i + p[1]][j + p[0]] = v + 1
                    except:
                        continue
            if arr[i][j] == 0:
                zero_cnt += 1
    if zero_cnt > 0:
        if before_zero_cnt == zero_cnt:
            print(-1)
        else:
            before_zero_cnt = zero_cnt
            tomato(v + 1)
    if zero_cnt == 0:
        MAX = max(map(max, arr))
        print(MAX -1)

tomato(1)



# https://www.acmicpc.net/problem/7569
# 토마토 1
