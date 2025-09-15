#  사용자로부터 점수를 입력받아 A B C D F 학점을 출력
score = int(input('총점을 입력하세요.'))
print(f'score = {score}')

if score >= 90:
    print('A') # 90~
elif score >= 80:
    print('B') # 80~89
elif score >= 70:
    print('C') # 70~79
elif score >= 60:
    print('D') # 50~59
else:
    print('F')


