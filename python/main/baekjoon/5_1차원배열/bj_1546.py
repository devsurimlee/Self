# https://www.acmicpc.net/problem/1546
import numpy as numpy

cnt = int(input())
score = list(map(int, input().split()))
result = 0;
maxScore = max(score)

for i in range(cnt):
    result += score[i] / maxScore * 100
print(result / cnt)


########################

# max(), min(), sum()

# for문 없이 하는 방법
print(sum(score) / maxScore * 100 / cnt)
# numpy로 평균 구하기
average = numpy.mean(score)
print(average / maxScore * 100)
