# 가위 바위 보 게임 (컴퓨터 vs. 휴먼)
# 가위:1  바위:2  보:3
# 규칙: 컴퓨터가 임의로 숫자를 선택  :random
# 인간이 숫자를 입력  : input
# 승패를 기록
# 3번 마다 계속할지 물어보기  : for

import random

game_count = 0
user_win = 0 

while True: 


    computer_number = random.randint(1,3)
    user_number = int(input("주먹:1 가위:2 보:3 중 하나를 입력하세요"))

    game_count += 1

    if computer_number == user_number : 
        print("비겼습니다") 

    elif (computer_number, user_number) in {(3,2),(2,1),(1,3)}:
        print("이겼습니다")
        user_win+=1
    else:
        print("졌습니다")



     #3번마다 사용자에게 계속 할건지 물어본다
    if game_count % 3 == 0:
        is_continue = input("계속하시겠습니까? (N/n)")
        if is_continue.lower() == 'n':
            print("실행이 중단되었습니다.")
            break

print(f"총 {game_count}판 중 {user_win}판 승리했습니다. 게임의 승률은 {(user_win/game_count)*100:.2f}% 입니다")


