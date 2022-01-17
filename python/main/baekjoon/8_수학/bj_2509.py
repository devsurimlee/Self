

# 최대공약수 구하기
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


i, j = map(int, input().split())
gcd = GCD(i, j)

print(gcd)
print(int(i * j / gcd))

# i * j = GCD * LCM
# LCM = i * j / GCD



#########################################
#
#
# https://www.acmicpc.net/problem/2609

# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
#
# 예제 입력 1
# 24 18
# 예제 출력 1
# 6
# 72