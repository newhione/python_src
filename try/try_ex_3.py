# 사용자 입력 처리 함수
# 함수: get_data()
# 파라미터
    # start: 시작값
    # end: 종료값
    # input_str: 가이드 문구
# 사용자 입력은 input
# return 점수로 변환된 입력값


def get_data(start, end, input_str='정수를 입력하세요.'):
    while True:
        try:
            h_num = int(input(f'{input_str}({start}~{end}): '))
            if  not (start <= h_num <= end):
                raise ValueError(f'({start}~{end}) 범위 초과')
            
        except Exception as e:
            print(f'오류: {e}')
        else:
            return h_num

# 랜덤 정수 - 컴퓨터가 선택한 값
import random as rd
start, end = 1, 10
computer = rd.randint(start, end)


count = 0
game_history = []

while True:
    count += 1
    human = get_data(start, end)

    # 게임
    if human > computer:
        print("크다")
        game_history.append((human, '크다'))
    elif human < computer:
        print("작다")
        game_history.append((human, '작다'))
    else:
        print("정답")
        print(f'시도 횟수: {count}')
        for guess_value, state in game_history:
            print(f'{guess_value} - {state}')
        print(game_history)
        break
