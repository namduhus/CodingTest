# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

A, X = map(int, input().split())

N = list(map(int, input().split()))

for num in N:
    if num < X:
        print(num, end=' ')