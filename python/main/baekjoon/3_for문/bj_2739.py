# https://www.acmicpc.net/problem/2739


x = int(input())
lists = range(1, 10)
for i in lists:
    print(x, "*", i, "=", i * x)
    
    # 파이썬 문자열은 + 대신 ,로 처리
