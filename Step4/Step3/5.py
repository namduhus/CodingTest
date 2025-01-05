# 책에는 long int는 4바이트 정수까지 저장할 수 있는 정수 자료형이고
# long long int는 8바이트 정수까지 저장할 수 있는 정수 자료형이라고 적혀 있었다

# 입력
# 첫 번째 줄에는 문제의 정수
# $N$이 주어진다

# 출력
# 혜아가
# $N$바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

N = int(input())

long_count = N // 4
result = "long " * long_count + "int"
print(result)
