# 6 2 10 3

x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))

# https://www.acmicpc.net/problem/1085 / 직사각형에서 탈출
