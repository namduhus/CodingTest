# 문제: BOJ 10811번 바구니 뒤집기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = list(range(1, N+1)) # ex input 1,2,3,4,5

for _ in range(M):
    i, j = map(int, input().split()) # i, j 위치 교환
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)
