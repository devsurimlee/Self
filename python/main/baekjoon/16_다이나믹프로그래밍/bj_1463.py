max = 10 ** 6
memo = [0 for i in range(max + 1)]
def circulation(max):
    memo[0] = 0
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1

    for i in range(4, max + 1):
        check = []
        if i % 2 == 0:
            check.append(memo[i // 2])
        if i % 3 == 0:
            check.append(memo[i // 3])
        check.append(memo[i - 1])

        memo[i] = min(check) + 1

circulation(max)
n = int(input())

print(memo[n])

# https://www.acmicpc.net/problem/1463 / 1로 만들기

# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
#
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
#
# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
#
# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
#
# 2 -> 1
# 10 -> 3 (10의 경우에 10 -> 9 -> 3 -> 1 로 3번 만에 만들 수 있다)
