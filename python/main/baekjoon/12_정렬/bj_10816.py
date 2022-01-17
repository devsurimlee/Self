import collections
import sys
input = sys.stdin.readline

_ = int(input())
N = sorted(map(int, input().split()))
_ = int(input())
M = list(map(int, input().split()))
#
# _ = 10
# N = sorted([6, 3, 2, 10, 10, 10, -10, -10, 7, 3])
# _ = 8
# M = [10, 9, -5, 2, 3, 4, 5, -10]

counter = collections.Counter(N)

for m in M:
    if counter.get(m):
        print(counter.get(m), end=' ')
    else:
        print(0, end=' ')




#####################

# 이진탐색 시간초과로 counter 이용함.

# result = []
#
# for each in m_list:
#     result.append(cnt_number(each))
#
# for r in result:
#     print(r, end=' ')


# 시간초과 1
# def cnt_number(num, start, end):
#
#     while start <= end:
#         mid = (start + end) // 2
#         cnt = 0
#         if num == n_list[mid]:
#             cnt += 1
#             n_list.remove(num)
#             return cnt + cnt_number(num, start, end - 1)
#
#         elif num > n_list[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0

# 시간초과 2
# def cnt_number(num):
#     start = 0
#     end = len(n_list) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#         cnt = 0
#         if num == n_list[mid]:
#             cnt += 1
#             n_list.remove(num)
#             return cnt + cnt_number(num)
#         elif num > n_list[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0

# https://www.acmicpc.net/problem/10816

# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
#
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
# 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
#
# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
#
# 예제 입력 1
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
# 예제 출력 1
# 3 0 0 1 2 0 0 2
