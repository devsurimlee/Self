# https://www.acmicpc.net/problem/1110

num = int(input())
tmp = num
result = 0
cnt = 0

while True:
    # 1의 자리, 기존 숫자끼리 더함
    right = ((tmp // 10) + (tmp % 10)) % 10
    result = (tmp % 10) * 10 + right
    cnt += 1
    if num == result:
        break
    else:
        tmp = result
print(cnt)



# 틀린 코드

while True:

    # tmp가 10일 경우 제대로 계산 X
    if tmp > 10:
        right = (tmp // 10) + (tmp % 10)
    else: right = tmp

    result = (tmp % 10) * 10 + (right % 10)
    cnt += 1
    if num == result:
        break
    else:
        tmp = result
print(cnt)
