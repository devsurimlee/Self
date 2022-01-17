import sys
import math

input = sys.stdin.readline
n = int(input())
li = map(int, input().split())
check = 0
n = 0
# li = range(1, 1000)

for num in li:
    if num == 2 or num == 3:
        check += 1
        # print(num, end=' ')
    elif num > 2 and num % 2 == 1:
        for i in range(3, int(math.sqrt(num) + 2), 2):
            if num % i == 0:
                break
            elif num % i != 0 and i >= int(math.sqrt(num)):
                check += 1
                # print(num, end=' ')

print(check)


# https://www.acmicpc.net/problem/1978

# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 4
# 1 3 5 7
#
# 3
