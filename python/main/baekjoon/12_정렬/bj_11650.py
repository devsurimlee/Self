import sys

n = int(input())
li = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split()) # [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]
    li.append([a, b])

sort_li = sorted(li, key=lambda i: (i[0], i[1])) # sorted 다중조건, 내림차순은 -붙이면 됨 (-i[0], i[1])

for x in sort_li:
    print(x[0], x[1])


# n = int(input())
# li = [[0, 0] for _ in range(n)]
#
# for i in li:
#     i[0], i[1] = map(int, sys.stdin.readline().split()) # [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]
#
# sort_li = sorted(li, key=lambda i: (i[0], i[1])) # sorted 다중조건, 내림차순은 -붙이면 됨 (-i[0], i[1])
#
# for x in sort_li:
#     print(x[0], x[1])

###########################
# 문제 좌표 정렬하기1

# https://www.acmicpc.net/problem/11650

# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3
#
# 1 -1
# 1 1
# 2 2
# 3 3
# 3 4

# https://dailyheumsi.tistory.com/67