import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
names = []

for i in range(n + m):
    each = input().strip()
    names.append(each)

a = set(names[:n])
b = set(names[n:])

result = list(a & b)
result.sort()

print(len(result))
for i in result:
    print(i)


# 리스트 합집합 list(a | b)
# 리스트 교집합 list(a & b)
# 리스트 차집합 list(a - b) - a에만 있는 요소
# 리스트 대칭차집합 list(a ^ b) - a, b 안겹치는거만 골라내기


##############################
# 처음에 푼 방식 240ms
# for문을 3번 사용
# 중복값을 이용하는 시도는 좋았으나 counter가 요소 개수로 잘라내지 못하므로 set과 list쓰는 편이 속도가 절반정도 줄었다.
# n, m = map(int, input().split())
# names = collections.Counter()
#
# for i in range(n + m):
#     each = input().strip()
#     names[each] += 1
#
# names = sorted(names.items(), key=lambda i: (-i[1], i[0]))
#
# li = []
# for name in names:
#     if name[1] > 1:
#         li.append(name[0])
#
# print(len(li))
# for l in li:
#     print(l)


# n = 3
# m = 4
# arr = ['ohhenrie', 'charlie', 'baesangwook', 'obama', 'baesangwook', 'ohhenrie', 'clinton']

# for i in range(n + m):
#     each = arr[i]
#     names[each] += 1


#############################
# https://www.acmicpc.net/problem/1764 // 듣보잡

# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
#
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
#
# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.
#
# 예제 입력 1
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton
# 예제 출력 1
# 2
# baesangwook
# ohhenrie
