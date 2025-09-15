students = []
class StudentMng:
    def __init__(self):
        self.name = ''
        self.age = 0

    def info_student(self):
        print(f'이름: {self.name}, 나이: {self.age}')

s1 = StudentMng()
s1.name = '홍혜원'
s1.age = 24
students.append(s1)

s2 = StudentMng()
s2.name = '이승협'
s2.age = 34
students.append(s2)

students[0].info_student()
students[1].info_student()
