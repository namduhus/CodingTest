# 백준 10813번 문제 공바꾸기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = list(range(1, N+1)) # ex input 1,2,3,4,5

for _ in range(M):
    i, j = map(int, input().split()) # i, j 위치 교환
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1] # 위치교환

print(*basket)
