import time

count = 0
while True:
    count += 1 
    print(f'{count}초')
    time.sleep(1) # 1초간 지연

    # 5초 단위로 사용자한테 계속 할건지 물어보기 "To be continue(Y/y)"
    # 1. 
    if count % 5 == 0:
        user_input = input("To be continue? (Y/N): ").upper()

        if user_input != 'Y':
            break
        

    # 2.                
    if count % 5 == 0:
        user_input = input("To be continue? (Y/N): ").upper()

        if user_input != 'Y':
            user_input = False    

