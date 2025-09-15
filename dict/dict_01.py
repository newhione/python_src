# 집합을 이루는 요소: 숫자, 문자, 문자열, list, set, tuple
list = [1, 1.5, "1", "1212", [1,2], (1,5,6), {2,3}]

# dictionary
# key와 value의 쌍으로 구성 {key:value, key:value}
# 순서가 없다
# key 중복X, 변하지 않는 자료형만 가능(문자열, 숫자, 튜플)
# CRUD(Create, Read, Use, Delet) 가능
# 각 요소에 접근할 때 -> key의 값으로 접근(index가 아님)
student = {
    "name" : "홍혜원",
    "age" : 23,
    "major" : "산업공학과"
}


# 읽기
print(f"student['name'] = {student['name']}") # student['name'] = 홍혜원

# 업데이트
student['name'] = '이승협'
print(f"student['name'] = {student['name']}") # student['name'] = 이승협

# 삭제
del student['name']
print(student) # {'age': 23, 'major': '산업공학과'}

# 추가 --> 없으면 추가, 있으면 업데이트
student['addr'] = '서울시 강남구'
print(student) # {'age': 23, 'major': '산업공학과', 'addr': '서울시 강남구'}