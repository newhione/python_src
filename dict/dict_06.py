# 딕셔너리의 정실을 이용한 list의 요소 카운트
# max함수를 이용해 기준을 value로 바꿔 가장 큰 value에 해당하는 키
# 매소드 .get() 

# key를 이용해서 value를 가져오는 방법
dict_1 = {'사과':10, '포도':20}

# 포도의 값 (인덱스 방법) --> 없으면 Keyerror
print(dict_1['포도']) #20

# (매소드 방법) --> 없으면 None
print(dict_1.get('포도')) #20
print(dict_1.get('파인애플')) #None

# 자료구조에서 가장 큰 값을 찾는 built-in 함수(내장 함수) `max`
print(max([1,2,3,4,5,6,7])) #7

dict_1 = {'국어':80, '국사':100}
print(max(dict_1))
print(max(dict_1, key=dict_1.get))

# 정렬
list_1 = [5,2,1,3]
print(sorted(list_1)) 
print(sorted(list_1, reverse=True))
print( sorted(list_1)[::-1]  )

# dict
dict_1 = {'국어':80,'국사':100,'영어':98,'수학':88}
print(sorted(dict_1))  # 키를 기준으로 정렬
print(sorted(dict_1, key=dict_1.get))  # value를 기준으로 키를 정렬