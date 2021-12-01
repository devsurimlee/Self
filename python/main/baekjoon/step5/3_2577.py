# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)

for i in range(10):
    print(num.count(str(i)))

# count: str에서 특정 문자 개수 return
