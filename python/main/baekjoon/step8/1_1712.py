# https://www.acmicpc.net/problem/1712

a, b, c = map(int, input().split())
cnt = 0

if b >=  c:
    print(-1)
else:
    cnt = a // (c - b) + 1
    print(cnt)

#############################
#
#  기존코드
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 21억 이하의 자연수이다.
#
a, b, c = map(int, input().split())
cnt = 1
isCheck = False

# A가 1부터 시작하므로 if문 없어도 됐음
if b > c or (a > 0 and b == c):
    print(-1)
elif a == 0 and b == c:
    print(1)
else:
    cnt = a // (c - b)
    # 처음엔 몫 계산 없이 cnt=1 시작으로 생각하고 while문 작성하였는데, 생각해보니 반복문이 필요없는 문제였음.
    while not isCheck:
        cost = a + (b * cnt)
        price = c * cnt

        if cost < price:
            isCheck = True
        else:
            cnt += 1
    print(cnt)


# 1000 70 170 -> 11
# 100 70 70