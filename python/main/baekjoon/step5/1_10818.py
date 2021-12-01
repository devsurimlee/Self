# https://www.acmicpc.net/problem/10818

limit = int(input())

# 입력값 int로 list
nums = list(map(int, input().split()))
# 배열 최소값, 최대값
print(min(nums), max(nums))

# 정렬해서 양끝값 가지고 오기
# 배열 역순 정렬 nums.sort(reverse=True)
nums.sort()
print(nums[0], nums[limit-1])
