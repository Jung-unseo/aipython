# 구구단 출력 프로그램

def print_gugudan(n):
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")

if __name__ == "__main__":
    # 사용자로부터 단을 입력 받음
    dan = int(input("몇 단을 출력할까요? "))
    print_gugudan(dan)
