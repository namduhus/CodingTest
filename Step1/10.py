# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

a = int(input())
b = int(input())

print(a * (b %10))
print(a * ((b // 10) % 10))
print(a * (b // 100))
print(a * b)