# https://www.acmicpc.net/problem/1620 / 나는야 포켓몬 마스터 이다솜
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

pokemon = {}
pokemon2 = {}
for i in range(n):
    name = input().rstrip()
    pokemon[name] = i + 1
    pokemon2[i + 1] = name

for i in range(m):
    find = input().rstrip()
    try:
        print(pokemon[find])
    except:
        print(pokemon2[int(find)])

