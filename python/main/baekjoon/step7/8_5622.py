# https://www.acmicpc.net/problem/5622

# 다이얼 배열로 담아서 이중for문 -> 속도가 떨어짐
dial_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

words = list(input())
sum = 0
delay = 3
for x in words:
    for dail in dial_list:
        if x in dail:
            sum += dial_list.index(dail) + delay

print(sum)


# 기존코드
#######################################
#
# words = list(input())
# sum = 0
# delay = 1
# for x in words:
#     if x in "ABC":
#         sum += 2
#     elif x in "DEF":
#         sum += 3
#     elif x in "GHI":
#         sum += 4
#     elif x in "JKL":
#         sum += 5
#     elif x in "MNO":
#         sum += 6
#     elif x in "PQRS":
#         sum += 7
#     elif x in "TUV":
#         sum += 8
#     elif x in "WXYZ":
#         sum += 9
#
# print(sum + (delay * len(words)))
