print( [ i for i in range(5) if i%2==0 ] )

list_1 = [1,2,3,1,2,3,5,4,8]
# 값 2에 해당하는 인덱스를 찾아 리스트로 반환
print( [ idx for idx, value in enumerate(list_1) if value == 2  ] )

age = 20
if age >= 18:
    print('성인')
else:
    print('미성년')

result = '성인' if age >= 18 else '미성년'
print(result)

list_2 = [10,24,13,53,31,29,17,54]
print( ['성인' if i >= 18 else '미성년' for i in list_2] )
