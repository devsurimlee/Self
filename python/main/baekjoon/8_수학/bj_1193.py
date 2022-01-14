# https://www.acmicpc.net/problem/1193

# 칸수 대각선으로 1씩 증가 = 1, 2, 3, 4, 5
# 홀수는 row/1, 짝수는 1/row로 시작

num = int(input())
row = 1
index = 0

if num == 1:
    print("1/1")
else:
    max = 1
    min = 0
    while True:
        row += 1
        max = max + row
        if max >= num:
            min = max - row + 1
            break

    # num=8, num_list = [7, 8, 9, 10], index = 1
    num_list = list(range(min, max + 1))
    index = num_list.index(num)

    # row 짝수
    if row % 2 == 0:
        print(f"{index + 1}/{row - index}")

    # row 홀수
    else:
        print(f"{row - index}/{index + 1}")
