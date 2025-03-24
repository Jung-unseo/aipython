# 사용자로부터 두 숫자를 입력 받음
a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

# 나눗셈의 경우, 분모가 0이 아닐 때만 수행
if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("0으로 나눌 수 없습니다.")