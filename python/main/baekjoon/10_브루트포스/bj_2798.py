# https://www.acmicpc.net/problem/2798

# n = 10
# m = 500
# lists = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]

n, m = map(int, input().split())
lists = list(map(int, input().split()))
isBreak = False
Sum = 0
lists.sort()

for x in range(n):
    if isBreak: break
    for y in range(x + 1, n):
        if isBreak: break
        for z in range(y + 1, n):
            tmp = lists[x] + lists[y] + lists[z]
            if tmp == m:
                Sum = m
                isBreak = True
                break
            if Sum < tmp < m:
                Sum = tmp

print(Sum)
