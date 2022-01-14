# https://www.acmicpc.net/problem/2438

a = int(input())

for i in range(1, a+1):
    for m in range(i):
        print("*", end='')
    print()