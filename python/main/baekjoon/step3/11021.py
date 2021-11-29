# https://www.acmicpc.net/problem/11021

leng = int(input())

for i in range(leng):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a+b}")
