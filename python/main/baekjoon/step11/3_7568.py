# https://www.acmicpc.net/problem/7568


n = 5
lists = [[55, 185, 0], [58, 183, 1], [88, 186, 2], [60, 175, 3], [46, 155, 4]]

# n = int(input())
# lists = []
# for i in range(n):
#     x, y = map(int, input().split())
#     lists.append([x, y, i])

lists.sort()
lists.reverse()
print(lists)

for i in range(n - 1):
    y1 = lists[i][1]
    y2 = lists[i][2]

    if y1 > y2:
        lists[i].append(i + 1)
    else:
        lists[i].append('?')

print(lists)




##################################

# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155
#
# 2 2 1 2 5