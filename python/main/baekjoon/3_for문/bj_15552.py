# https://www.acmicpc.net/problem/15552

# limit = int(input())
#
# for i in range(limit):
#     a, b = map(int, input().split())
#     print(a+b)

import sys

limit = int(sys.stdin.readline())
for i in range(limit):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

