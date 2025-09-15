# 함수
# 함수명 add
# 파라미터 2개 op1, op2
# 결과 반환

# 생성
def add(op1,op2):
    result = op1 + op2
    return result

# 사용
numbers = [add(10,20), add(10,20), add(10,20)]
print(numbers)

# ---------------------------------------------------
# 매개변수를 받아 출력하는 함수
# 함수명: show_number
# 매개변수명: data

# 1. 생성
def show_number(data):
    print(f'numbers = {data}')

# 1. 사용
show_number(add(10,2))

# 2. 생성
def show_number2(data):
    return f'numbers={data}'

# 2. 사용
print(show_number(add(10,2)))

