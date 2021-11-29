# https://www.acmicpc.net/problem/11022

leng = int(input())

for i in range(leng):
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1, a, b, a+b))