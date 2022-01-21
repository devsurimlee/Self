n, k = map(int, input().split())

def factorial(cnt):
    if cnt <= 1:
        return 1
    return cnt * factorial(cnt - 1)


result = int(factorial(n) / factorial(n - k) / factorial(k))
print(result)

#########################
# nCk = n! / (n-k)!k!

# https://www.acmicpc.net/problem/11050 / 이항계수

# 자연수 (N)과 정수 (K)가 주어졌을 때 이항 계수
# (binom{N}{K})를 구하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 (N)과 (K)가 주어진다. (1 ≤ (N) ≤ 10, 0 ≤ (K) ≤ (N))
# 
# 출력
# 
# (binom{N}{K})를 출력한다.
# 
# 예제 입력 1
# 5 2
# 예제 출력 1
# 10
