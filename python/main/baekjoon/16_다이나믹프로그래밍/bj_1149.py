import sys

input = sys.stdin.readline

n = int(input())
# case = ['30 19 5', '64 77 64', '15 19 97', '4 71 57', '90 86 84', '93 32 91']
# case = ['3 2 1', '1 1 1', '1 100 100']
house = []

for i in range(n):
    # house.append(list(map(int, case[i].split())))
    house.append(list(map(int, input().split())))

for i in range(1, n):
    a = min(house[i - 1][0], house[i - 1][1])
    b = min(house[i - 1][1], house[i - 1][2])
    c = min(house[i - 1][0], house[i - 1][2])

    house[i][0] += b
    house[i][1] += c
    house[i][2] += a

print(min(house[-1]))

####################################
# 기존에 풀던 흔적
# 이대로 돌리면 중복값 마주쳤을 때 대응이 안됨
# 순서대로 더하는 것만 생각했는데, 거꾸로 더하니까 인덱스 정보도 필요없고 깔끔하게 해결됨.

# memo = [0, 0, 0]

# for i in range(3):
#     memo[i] = house[0][i]
#     index = i
#     for j in range(1, n):
#         if index == 0:
#             memo[i] += min(house[j][1], house[j][2])
#             index = house[j].index(min(house[j][1], house[j][2]))
#         elif index == 1:
#             memo[i] += min(house[j][0], house[j][2])
#             index = house[j].index(min(house[j][0], house[j][2]))
#         elif index == 2:
#             memo[i] += min(house[j][0], house[j][1])
#             index = house[j].index(min(house[j][0], house[j][1]))

# print(min(memo))

###############################################

# https://www.acmicpc.net/problem/1149
# RGB거리
