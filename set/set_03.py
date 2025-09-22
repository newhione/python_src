# 집합연산
import random
list_a = random.sample(range(10), 7) # 0~10 중복되지 않은 임의의 7개
list_b = random.sample(range(10), 7)

# 중복을 허용하면서 0~10 임의의 7개
# random.randint(0,10) --> 임의의 1개
list_c = []
for i in range(7):
    list_c.append(random.randint(0,10))


# 합집합 or
    # 연산자 ㅣ
set_a = {1,2,3,4,5}
set_b = {2,3,6,7,8}
union_set_1 = set_a | set_b 
    # 메서드 .union()
union_set_2 = set_a.union(set_b)

print(union_set_1)
print(union_set_2)

# 교집합 and
    # 연산자 &
intersection_set_1 = set_a & set_b
    # 메서드 .intersection()
intersection_set_2 = set_a.intersection(set_b)

print(intersection_set_1)
print(intersection_set_2)

# 차집합
    # 연산자 -
difference_set_1 = set_a - set_b
    # 메서드 .difference()
difference_set_2 = set_a.difference(set_b)

print(difference_set_1)
print(difference_set_2)