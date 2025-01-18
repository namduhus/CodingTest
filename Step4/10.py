# 문제: BOJ 1546번 평균

N = int(input())

scores = list(map(int, input().split()))

M = max(scores)

new_scores = [(score / M) * 100 for score in scores]

print(sum(new_scores) / N)
