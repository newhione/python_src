# 리스트 컴프리핸션
# total = [ ]
# for i in range(1,11):
#     total.append(i)

# print(total)

print([i for i in range(1,11)])   #간단한 거는 한 줄로 표현

import random
random.randint(1,10)

total = []
for i in range(5):
    total.append(random.randint(1,10))

print(total)

print( [random.randint(1,10) for i in range(5)] )