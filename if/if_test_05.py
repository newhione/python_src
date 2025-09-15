# 논리 연산자 사용
# 나이가 18이상(성인)이면서 주민번호를 가진 사람은 "입장가능", 그렇지 않으면 "입장불가"

has_id = True
age = int(input('나이를 입력하세요:'))


if age >=18 and has_id == True:
    print('입장 가능')

else:
    print('입장 불가능')

print('종료')