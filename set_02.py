# 집합연산
import random
list_a = random.sample(range(10), 7)
list_b = [1,3,3,1,1,5,7,1,2,2,4]
find_list = []
for a in list_a:
    for b in list_b:
        if a == b:
            find_list.append(a)
print(f'list_a = {list_a}')
print(f'list_b = {list_b}')
print(f'find_list = {find_list}') # find_list = [5, 7, 1, 1, 1, 1]
print(f'set(find_list) = {set(find_list)}') # set(find_list) = {1, 5, 7}

# line 13에서 set을 사용하지 않고 원래 로직(line 6~9)을 계산해
# find_list에 중복값이 저장되지 않도록
