#def print_cat():
#    cat = [
#        " /\_/\  ",
#        "( o.o )",
#        " > ^ < "
#    ]
#    for line in cat:
#        print(line)

#def print_dog():
#    dog = [
#        " /\\_/\\ ",
#        "( •ᴥ• )",
#        " /︶\\ "
#    ]
#    for line in dog:
#        print(line)

#def print_rabbit():
#    rabbit = [
#        " (\_/) ",
#        "( •_• )",
#        "/ >🍎 "
#    ]
#    for line in rabbit:
#        print(line)

#print("그림 출력 프로그램")
#print("====================")
#print("1. 고양이")
#print("2. 강아지")
#print("3. 토  끼")
#print("====================")

#try:
#    n = int(input("선택: "))
#    if n == 1:
#        print("고양이 그림")
#        print_cat()
#    elif n == 2:
#        print("강아지 그림")
#        print_dog()
#    elif n == 3:
#        print("토끼 그림")
#        print_rabbit()
#    else:
#        print("1~3 중에서 선택해주세요.")
#except ValueError:
#    print("숫자를 입력해주세요.")

    
def print_cat():
    cat = [
        " /\_/\  ",
        "( o.o )",
        " > ^ < "
    ]
    for line in cat:
        print(line)

def print_dog():
    dog = [
        " /\\_/\\ ",
        "( •ᴥ• )",
        " /︶\\ "
    ]
    for line in dog:
        print(line)

def print_rabbit():
    rabbit = [
        " (\_/) ",
        "( •_• )",
        "/ >🍎 "
    ]
    for line in rabbit:
        print(line)

while True:
    print("\n그림 출력 프로그램")
    print("====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토  끼")
    print("0. 종료")
    print("====================")

    try:
        n = int(input("선택: "))
        if n == 0:
            print("프로그램을 종료합니다.")
            break
        elif n == 1:
            print("고양이 그림")
            print_cat()
        elif n == 2:
            print("강아지 그림")
            print_dog()
        elif n == 3:
            print("토끼 그림")
            print_rabbit()
        else:
            print("1~3 중에서 선택해주세요.")
    except ValueError:
        print("숫자를 입력해주세요.")


