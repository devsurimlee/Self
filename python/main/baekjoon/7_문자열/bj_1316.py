# https://www.acmicpc.net/problem/1316

limit = int(input())
sum = limit

for i in range(limit):
    words = input()

    for m in range(len(words) - 1):
        if words[m] != words[m + 1] and words[m + 1:].count(words[m]) > 0:
            sum -= 1
            break
print(sum)

# abcabc
# happy

# [unsolved] 해당 문제의 경우 조건에 안맞는 경우가 더 많으므로, 점수를 빼는 형식으로 하면 더 빨리 풀수있음

