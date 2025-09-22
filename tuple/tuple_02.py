# 튜플
# 읽기 전용, 변경 불가능
tuple_1 = (1,2,3,4,1,5,4,1,4,6)
# tuple_1[0] = 100
# print(tuple_1) --> TypeError: 'tuple' object does not support item assignment
tuple_1.count(1)
print(tuple_1.count(4))
print(tuple_1.index(4)) # 값 4가 처음으로 나타나는 인덱스 반환
print(tuple_1[4]) # 튜플의 인덱스 4에 있는 값을 출력


# 튜플 vs. 리스트
# 리스트: 서로 변경 가능
# 튜플: 변경 불가능
# 튜플 -> 리스트 (0), 리스트 -> 튜플 (0)
