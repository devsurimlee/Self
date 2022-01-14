# https://www.acmicpc.net/problem/2562

nums = []

for i in range(9):
    nums.append(int(input()))       # 배열 끝에 원소 추가

max = max(nums)
print(max)
print(nums.index(max) + 1)
