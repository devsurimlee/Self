# https://www.acmicpc.net/problem/2292

# 1
# 7-2 -> 5
# 19-8 -> 11
# 37-20 -> 17
# 61-38 -> 23
#
# 11-5 -> 6
# 17-11 -> 6
# 23-17 -> 6
# 다음 둘레줄은 이전값 + 6

# 1 , 1 + (6*1), (1+6)+ 6*2, (1+6+6+6)+6*3, ((1+6+6+6)+6*3) + 6*4, ...

room = int(input())
angle = 6
sum = 1

# room = 1인경우 case 추가함
if room == 1:
    print(room)
else:
    for x in range(1, room):
        sum = sum + (angle * x)
        if sum >= room:
            print(x + 1)
            break

