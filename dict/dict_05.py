# 선거 시스템
# 유권자들은 기호로 투표를 진행, 결과를 list에 저장
# ex) 1,2,3
# 투표는 순환문을 이용해 유권자가 10이라면 10번 순환하며 후보자(1~5) 선택
# [1,1,2,3,4,1,5,1]
# 리스트에 있는 번호의 횟수를 구해 당선자 출력
candidate = ['이승협','김재현','차훈','유회승','서동성']
vote = []
counts = 10 # 유권자 수
result = {} # 투표용지 카운트



for _ in range(10):
    vote.append(int(input('투표를 하세요(1~5): ')))

# dict 이용
for i in vote:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

print(f'result = {result}')

max_key =  max(result, key=result.get )
# 당선자  key - 1
print(f'당선자 : {cadidate[max_key-1]} 득표수 : {result[max_key]}')
