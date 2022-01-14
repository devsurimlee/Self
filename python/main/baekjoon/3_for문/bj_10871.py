# https://www.acmicpc.net/problem/10871

a, b = map(int, input().split())
lists = input().split()

for i in range(a):
    if b > int(lists[i]):
        print(int(lists[i]), end=' ')