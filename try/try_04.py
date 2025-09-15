# raise 예외 발생하기
try:
    print("정상코드")
    print("예외발생")
    # raise "내가 발생시킨 오류"
    raise ValueError("test")
except Exception as e:
    print(f'Error: {e}  {e.__class__}  {e.__class__.__name__}')

# ---------------------------------------------------------------------------------
def check_number(num):
    if num % 2 != 0: # 숫자가 홀수일 경우
        raise Exception("짝수만 입력해야 합니다.") # 'Exception' 예외를 발생시킴
    else:
        print("짝수가 입력되었습니다.")

# 예외가 발생하는 경우
try:
    check_number(7)
except Exception as e:
    print(f"에러 발생: {e}") # 에러 메시지 출력  # 에러 발생: 짝수만 입력해야 합니다.

# 예외가 발생하지 않는 경우
check_number(4) # 짝수가 입력되었습니다.