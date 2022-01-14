# https://www.acmicpc.net/problem/2908

a, b = input().split()

a = ''.join(reversed(a))
b = ''.join(reversed(b))

print(a if a > b else b)


# #input 뒤집어서 받음
# a, b = input()[::-1].split()
# print(a if a > b else b)

# string만 가능
# '1234'[::-1] -> 4321
