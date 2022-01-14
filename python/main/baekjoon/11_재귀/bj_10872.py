# https://www.acmicpc.net/problem/10872


def factorial(cnt):
    if cnt <= 1:
        return 1
    return cnt * factorial(cnt - 1)

print(factorial(int(input())))
