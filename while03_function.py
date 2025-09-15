import time

count = 0
is_continue = True

def display_second(count):
    count += 1
    print(f'{count}초')
    time.sleep(1)
    return count


def is_user_continue(count):
    if count % 5 == 0:
        user_input = input('To be continue?(Y/N)').upper()
        if user_input == 'Y':
            return True
        else:
            return False
    return True


while is_continue:
    count = display_second(count) # 1초 간격으로 출력
    is_continue = is_user_continue(count) # 5초 간격으로 진행여부 판단


# 디버깅 방법
# break point -> Python Debugger: Debug Python File -> F10(하나씩 실행)


