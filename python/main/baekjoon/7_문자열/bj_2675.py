# https://www.acmicpc.net/problem/2675


a = int(input())

for i in range(a):
    cnt, word = input().split()
    result = ''

    for m in list(word):
        result += m * int(cnt)      # 문자열 곱하기 가능

    print(result)


# 2         <- 테스트케이스 개수
# 3 ABC
# 5 /HTP




