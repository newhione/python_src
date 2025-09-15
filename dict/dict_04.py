staff = {
    '홍길동': {
        '직책': '매니저',
        '연봉': 200000000,  # 쉼표 제거
        '경력': {
            '삼성전자': 5,
            '엘지전자': 3,
            'sk': 10
        },
        '취미': ['낚시', '헬스', '수영', '자전거']
    }
}

print(staff['홍길동']['경력']['삼성전자'])  # 5
print(staff['홍길동']['취미'][-1]) #자전거

# 학생이 가지는 과목이 3개이고 국어, 영어, 수학 점수로 관리 
student1 = [100,80,90]
student2 = [90,85,90]
student3 = ['국어':100,'영어':100,'수학':85]
student4 = ['영어':100,'국어':100,]
element_class = [student3, student4, studnet5]

total_math = 0
for student in element_class:
    total_math +=student['수학']