# https://www.acmicpc.net/problem/2439

a = int(input())

# 이중 for문
for i in range(a):
    for m in range(a, 0, -1):
        if m > i + 1:
            print(end=' ')
        else:
            print('*', end='')
    print()

# 문자열도 * 이용하면 연산 가능함
for i in range(1, a + 1):
    str = '.' * (a - i) + "*" * i
    print(str)
