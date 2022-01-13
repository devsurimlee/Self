
import sys
import collections

# 최빈값 구하는 함수
def mode(li):
    if len(li) == 1:
        return li[0]

    cnt = collections.Counter(li)
    cnt_list = [cnt.most_common()[0][0]]  # 최빈값 1개 넣고 시작

    for i in range(len(cnt) - 1):
        if cnt.most_common()[i][1] == cnt.most_common()[i + 1][1]:
            cnt_list.append(cnt.most_common()[i + 1][0])
        else:
            break

    if len(cnt_list) == 1:
        return cnt_list[0]
    else:
        return sorted(cnt_list)[1] # 두번째로 작은값 리턴

#########################################

n = int(input())
li = []
for i in range(n):
    num = int(sys.stdin.readline())
    li.append(num)

li.sort()
SUM = round(sum(li) / n)

print(SUM)  # 평균값
print(li[n // 2])  # 중앙값
print(mode(li))  # 최빈값
print(li[-1] - li[0])  # 범위

li = [3, 1, 2, 0, 1, 4]


# https://www.acmicpc.net/problem/2108

# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
#
# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.


# 5
# 1
# 3
# 8
# -2
# 2
#
# 2
# 2
# 1
# 10
###############
# 1
# 4000
#
# 4000
# 4000
# 4000
# 0
