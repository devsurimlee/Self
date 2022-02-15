# N, r, c = 10, 512, 512
N, r, c = map(int, input().split())

width = 2 ** N
cnt = 0
box = [[0, 1], [2, 3]]

def check(num, r, c):
    global cnt

    if num == 2:
        a = r % 2
        b = c % 2
        cnt += box[a][b]
        print(cnt)
        return cnt

    num = num // 2
    if r < num and c < num:         # 1분기
        check(num, r, c)
    elif r < num <= c:              # 2분기
        cnt += num * num
        check(num, r, c - num)
    elif r >= num > c:              # 3분기
        cnt += (num * num) * 2
        check(num, r - num, c)
    elif r >= num and c >= num:     # 4분기
        cnt += (num * num) * 3
        check(num, r - num, c - num)

check(width, r, c)

# □ □ □ □
# □ □ □ □
# □ □ □ □
# □ ■ □ □


# https://www.acmicpc.net/problem/1074 / Z


