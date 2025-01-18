import sys
input = sys.stdin.readline

# set()연산은 집합 연산
student = set(range(1, 31)) # 1 ~ 30번 학생의 번호를 모두 포함하는 집합

submitted_student = set()
for _ in range(28):
    submitted_student.add(int(input().strip()))

missing_student = sorted(student - submitted_student)

for student in missing_student:
    print(student)
