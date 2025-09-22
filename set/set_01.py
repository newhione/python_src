# 저금통
list_a = [100,500,10,500,100,50,500,10]
# 저금통에 있는 동전의 종류 10,50,100,500

# set
# 중복을 제거(허용하지 않는다)
set_a = {1,2,3,1,2,3,1} # {1, 2, 3}
print(set_a)
print(set(list_a)) # {10, 50, 100, 500}

set_b = {1,2,3}
# print(set_2[0]) --> TypeError: 'set' object is not subscriptable, set는 중복이 제거되므로 순서를 보장하지 않음. pandas에서 사용 가능

set_b.add(4)
print(set_b) # {1, 2, 3, 4}

set_b.remove(1)
print(set_b) # {2, 3, 4}

set_b.pop()
print(set_b) # {3, 4} --> set은 순서가 없으므로, 마지막 원소가 아닌 임의의 원소를 제거함
print(set_b.pop())