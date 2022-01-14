# https://www.acmicpc.net/problem/2884

a, b = map(int, input().split())
minus = 45

if b < minus:
    b += 60
    a -= 1
b -= minus

if a < 0:
    a += 24

print(a, b)
