# 중첩 for2

list_1 = [1,2,3]
list_2 = [10,20,30,490]

list_2th = [list_1, list_2]

for i in range(len(list_2th)):
    for j in range(len(list_2th[i])):
        print(f'list_2th[{i}][{j}]  {list_2th[i][j]}')


# for문: 반복 횟수가 지정되어 있음.
# while문: 횟수가 지정되어 있지 않음!!