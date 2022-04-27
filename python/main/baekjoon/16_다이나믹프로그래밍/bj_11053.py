# n = int(input())
# nums = list(map(int, input().split()))

n = 6
nums = (10, 20, 10, 30, 20, 50)

dp = [1 for x in range(n)]
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


# https://www.acmicpc.net/problem/11053 / 가장 긴 증가하는 부분 수열
# 가장 작은 수의 경우 1이므로 1로 시작함.