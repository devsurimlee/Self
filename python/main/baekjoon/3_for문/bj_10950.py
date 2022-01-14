# https://www.acmicpc.net/problem/10950

length = int(input())

for i in range(length):
    a, b = map(int, input().split())
    print(a+b)