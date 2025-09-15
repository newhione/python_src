# remove
list_a = [1,1,1,2,1,45,3,2,1,5,5]

# list_a.remove(5) --> ValueError: list.remove(x): x not in list
# list_a.remove(1)
# print(list_a)


# 1. Solution: 거꾸로 가는 방법
for i in range(len(list_a)-1,-1,-1):
    if list_a[i] == 1:
        del list_a[i]

print(list_a)


# remove() 이용하기 ->  완벽하게 1이 제거가 안됨.
# for i in list_a:
#     if i in list_a: # i가 list_a에 없으면 오류나기 때문에
#         list_a.remove(1) # 가장 먼저 만나는 1만 제거함
# print(list_a)
list_a = [1, 1, 1, 2]

for i in range(len(list_a)):
    if i in list_a:
        list_a.remove(1)

print(list_a)


list_b = [1,1,1,2,2,2,2,3,3,3]
for i in range(len(list_b)):
    print('*')
    if i in list_b:
        list_b.remove(1)
    else:
        break


# 3. Solution: append() 이용하기
list_a = [1, 1, 1, 2]
result = []

for x in list_a:
    if x != 1:          # 1이 아닌 경우만
        result.append(x)

print(result)  # [2]

# 순환하면서 기존 list가 변하지 않는 것이 가장 best
# for문 안에서는 list 자체는 변경하지 않는 방향으로 logic를 짜야함. (우리가 생각하는 기존 순환 구조가 깨짐)


# 연습문제
numbers = [273,103,5,32,65,9,72,800,99]

for number in numbers:
    if number >= 100:
        print("- 100이상의 수:", number)