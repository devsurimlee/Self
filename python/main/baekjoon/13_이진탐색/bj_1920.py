import sys

def binary_search(num):

    start = 0
    end = len(n_li) - 1

    while start <= end:
        median = (start + end) // 2

        if n_li[median] == num:
            return True
        elif n_li[median] < num:
            start = median + 1
        else:
            end = median - 1
    return False

n = sys.stdin.readline()
n_li = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_li = map(int, sys.stdin.readline().split())

for num in m_li:
    if binary_search(num) :
        print(1)
    else:
        print(0)

##############

# 이진탐색
# 탐색값과 리스트가 있으면 리스트 중앙값을 기준으로 탐색
# 리스트는 정렬 필수
#
# target = 12
# list = [1, 8, 12, 24, 100, 105, 200, 205, 233]

# start1 = 0
# end1 = 8
# mid1 = 0+8 // 2 = 4
# list[mid] = 100

# 12 < 100이므로 왼쪽으로 탐색함
#
# 0~3 사이 중간값 잡음
#
# start2 = 0
# end2 = 4 - 1 = 3
# mid2 = 0+3 // 2 = 1
# list[mid2] = 8
#
# 12 > 8이므로 오른쪽으로 탐색함
#
# start3 = 1 + 1 2
# end3 = 3
# idx3 = 2+3 // 2 -> 2
#
# list[2] = 12 찾음!
#



# ======================
# 전체탐색으로 시간초과
# import sys
#
# n = sys.stdin.readline()
# n_li = sys.stdin.readline()
# m = int(sys.stdin.readline())
# m_li = list(sys.stdin.readline().split())
#
# for num in m_li:
#     if n_li.count(num) > 0:
#         print(1)
#     else:
#         print(0)

# https://www.acmicpc.net/problem/1920 // 수찾기

# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
#
# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 5         -> N
# 4 1 5 2 3 -> N개 정수
# 5         -> M
# 1 3 7 9 5 -> M개 정수
#
# 1
# 1
# 0
# 0
# 1