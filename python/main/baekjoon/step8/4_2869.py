import math

a, b, v = map(int, input().split())
i = math.ceil((v - b) / (a - b))

print(i)

# =====================
# 시간초과
# 소수점 올림으로 해결하면 되는 문제였음.
# round() -> 반올림, meth.ceil() 올림 함수
#
# run = a - b
# i = round(v / run)
#
# while True:
#     today = run * (i - 1) + a
#     before = (run * (i - 2)) + a
#     if today >= v > before:
#         print(i)
#         break
#     else:
#         i -= 1
