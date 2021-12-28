# https://www.acmicpc.net/problem/7568


n = int(input())
lists = []
for i in range(n):
    x, y = map(int, input().split())
    lists.append([x, y])


for i in lists:
    rank = 1
    for m in lists:
        if i[0] < m[0] and i[1] < m[1]:
            rank += 1
    print(rank, end=" ")
    

##################################

# case1
# n = 5
# lists = [[55, 185, 0], [58, 183, 1], [88, 186, 2], [60, 175, 3], [46, 155, 4]]  # 2 2 1 2 5

# case2
# n = 3
# lists = [[4, 1], [5, 10], [6, 1]]  # 2 1 1

# case2가 3 1 1이 아니고 2 1 1인점에 주목.
# 각자 자기보다 큰 덩치 수로 따지므로 [4, 1]은 [6, 1]과 같은 체급이다! 그래서 3등이 아니고 2등임 <- 이부분 이해가 어려웠음 ㅠ


