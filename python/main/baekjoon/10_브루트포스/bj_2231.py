# https://www.acmicpc.net/problem/2231


n = int(input())
# n = 216

for i in range(n):

    total = i + sum(map(int, list(str(i))))
    if total == n:
        print(i)
        break
    if i == n - 1:
        print(0)

# n = int(input())
# # 216 - 3 * 9, 216+1 -> 189~217
# for m in range(n - len(str(n)) * 9, n + 1):
#     sum = m
#     temp = m
#     while m > 0:
#         sum += m % 10
#         m //= 10
#     if sum == n:
#         print(temp)
#         exit()
# print(0)


# 216 - > 198  // 198+1+9+8 = 216, 생성자M = 198, 생성자 없으면 0
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
