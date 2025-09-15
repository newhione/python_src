# list, set, tuple, dict
result = dict([ ['name', '홍혜원'], ['age', 23] ])
print(type(result))
print(result)

# -----------------------------------------------------
# 두 개의 list
# 한 개는 key에 해당하는 값들의 집합, 다른 하나는 value에 해당하는 집합
# dic 구조로 만들기
names = ['이승협', '유회승', '김재현']
scores = [100, 99, 98]

# 1. 비어있는 dict 변수 생성 -> 변수['key'] = value 형태로 생성 -> 순환문을 통해 반복
students_1 = {}
count = 0

for name in names:
    students_1[name] = scores[count]
    count += 1    # 다음 점수를 가리키도록 인덱스를 하나 증가
print(students_1)
# -----------------------------------------------------

students_2 = {}

for i in range(len(names)):
    students_2[names[i]] = scores[i]

print(students_2)