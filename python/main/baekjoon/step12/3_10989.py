import sys

n = int(input())
li = [0] * 100001

for _ in range(n):
    num = int(sys.stdin.readline()) # 3이면 3번째에 담음
    li[num] += 1

for i in range(len(li)):
    if li[i] > 0:
        for _ in range(li[i]):
            print(i)


############################
# 메모리초과남
# 다 담고 숫자 카운팅하는게 아니라, 배열 선언해놓고 바로 그자리에 카운팅하면 for문 한번 덜 해도됨

# n = int(input())
# li = []
# count_li = []
# for _ in range(n):
#     li.append(sys.stdin.readline())
#
# for i in range(n):
#     count_li.append(li[i].count(i))
#
# for x in count_li:
#     for _ in range(x):
#         print(x)


# https://www.acmicpc.net/problem/10989

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 카운팅 알고리즘
