# 0~100 사이의 랜덤한 숫자 10개를 리스트로 저장
import random
numbers = random.sample(range(100),10)


# numbers 중 짝수만 찾아 새로운 리스트에 저장
# 1. 리스트를 순환한다
# 2. 순환하면서 각 data가 짝수인지 판단
# 3. 짝수이면 미리 준비한 빈 list에 추가
# 4. for문이 종료되면 준비한 list를 출력하고, len()을 통해 개수를 확인
even_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print(f'짝수 집합 : {even_numbers}, 개수 : {len(even_numbers)}')
