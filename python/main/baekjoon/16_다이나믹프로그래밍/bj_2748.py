n = int(input())

def fibo():
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1

    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    print(memo[n])

if n == 0:
    print(0)
elif 0 < n < 2:
    print(1)
else:
    memo = [0] * (n + 1)
    fibo()


######################################

# https://www.acmicpc.net/problem/2748
# 피보나치수 2
