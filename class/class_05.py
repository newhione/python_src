# 학생
# 이름, 과목과 정수, 학생정보 출력, 총점, 평균, 학점
# 변수: 이름, 과목과 점수, 총점, 평균, 학점
# 함수: 학생정보 출력, 총점함수, 평균함수, 학점함수

students = [ ] #학생이름 저장

def info_student(student): #학생 1명의 정보(딕셔너리)를 받아 이름과 나이를 출력하는 함수
    print(f"이름: {student['name']}, 나이: {student['age']}") #딕셔너리에서 'name', 'age' 키에 해당하는 value

#학생정보 입력
def create_student(name, age): #학생 정보를 딕셔너리 형태로 만들어서 반환하는 함수
    return {'name':name, 'age':age} #딕셔너리 생성

#students 리스트에 학생 정보를 직접 추가 -> students 리스트 안에는 두 개의 딕셔너리가 들어감
students.append(
    {'name':'홍혜원', 'age':24}
)
students.append(
    {'name':'이승협', 'age':34}
)

# 모든 학생 출력
for s in students:
    info_student(s)