import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

for i in sorted(arr):
    sys.stdout.write(str(i) + '\n')         # 한줄씩 개행


########################
#
# python으로 실행시 시간초과 뜸 -> pypy3으로 제출
# n = int(input())
# arr = []
#
# for _ in range(n):
#     arr.append(int(input()))
#
# arr.sort()
#
# for i in range(n):
#     print(arr[i])


# https://www.acmicpc.net/problem/2751

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
