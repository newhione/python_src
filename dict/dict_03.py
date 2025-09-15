# 딕셔러니 생성
# 딕셔러니에서 값을 출력
# 딕셔너리에서 값을 추가
# 딕셔너리 삭제

# 딕셔너리 특정 키의 데이터 수정
# enumerate(), zip(), .items(), .keys(), .values()
# map(), 정렬 --> 람다함수 적용
# 함수의 파라미터 - 키워드 파라미터, 가변 키워드 파라미터

# dict_01 연습
my_bag = {'필통':'주황색', "공책":"영어공책",'지갑':'갈색'}
print(my_bag)

# 가방에서 필통을 꺼내 출력
print(my_bag['필통'])

# 가방에서 공책을 꺼내 출력
print(my_bag['공책'])

# 지갑을 빨강색으로 변경
my_bag['지갑'] = '빨강색'
print(my_bag)

# 하얀색 물통 추가
my_bag['물통'] = '하얀색'
print(my_bag)

# 공책 버리기
del my_bag['공책']
print(my_bag)

# 순환문과 연결
for i in my_bag:
    print(i, my_bag[i]) # 필통 주황색
                        # 지갑 빨강색
                        # 물통 하얀색