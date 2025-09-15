# number_input_a = int(input("정수 입력: ")) # 정수를 입력하지 않았을 경우, 예외 발생

# print("원의 반지름:", number_input_a)
# print("원의 둘레:", 2*3.14*number_input_a)
# print("원의 넓이:", 3.14*number_input_a*number_input_a)

# 예외 처리 (오류를 피해가는 행위)
# try:
    # 예외가 발생할 가능성이 있는 코드
# except:
    # 예외가 발생했을 때 실행할 코드
# else:
    # 예외가 발생하지 않았을 때 실행할 코드
# finally:
    # 무조건 실행할 코드
try:
    num1, num2 = map(int, input("공백을 기준으로 두개의 숫자를 입력하세요: ").split())
    calc_lists = [num1+num2, num1-num2, num1*num2, num1/num2]

    print('1. 더하기', end='\t')
    print('2. 빼기', end='\t')
    print('3. 곱하기', end='\t')
    print('4. 나누기')
    
    choice = int(input("\n원하는 계산을 선택하세요(1~4): "))

    if choice == 1:
        print("결과:", calc_lists[0])
    elif choice == 2:
        print("결과:", calc_lists[1])
    elif choice == 3:
        print("결과:", calc_lists[2])
    elif choice == 4:
        print("결과:", calc_lists[3])
    else:
        print("1~4 중에서 선택하세요!")

except ValueError:
    print("숫자를 정확히 입력하세요. (예: 10 2)")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print("알 수 없는 오류 발생:", e)

finally:
    print("프로그램 종료")


