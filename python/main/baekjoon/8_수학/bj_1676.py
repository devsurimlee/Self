from functools import reduce


n = int(input())
if n == 0:
    print(0)
else:
    factorial = reduce(lambda x, y: x * y, range(1, n + 1))
    factorial = list(str(factorial))[::-1]

    for i in range(len(factorial)):
        if factorial[i] != '0':
            print(i)
            exit(0)



# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수
