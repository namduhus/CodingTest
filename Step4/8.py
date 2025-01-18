# 문제: BOJ 3052번 나머지

import sys
input = sys.stdin.readline

remainders = set()

for _ in range(10):
     num = int(input().strip())
     remainders.add(num % 42)

print(len(remainders))
