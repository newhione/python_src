# 딕셔너리
    # .items()  .keys()  .values()
dict_1 = {}
# 정렬
    # sorted()
# max
    # max() 
# enumerate
    # 순환문에서 리스트를 감싸면 (index, list의 값)   
# zip()
    # 여러 개의 iterable들을 각 원소를 쌍으로 하는 집합
    # (1,2), ('사과', '배')
    # [(1,'사과'), (2,'배')]
# map()
    # map(함수명, iterable)
    # iterable한 객체의 각 요소에 함수를 적용하는 것
    # map(int, ['1','2']) -> [1,2]

import collections
data = [1,1,1,1,2,1,3,4,1,2,4,1]
print(collections.Counter(data))