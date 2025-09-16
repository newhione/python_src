# 클래스 콜백 함수
# __eq__ : ==
# __ne__ : !=
# __lt__ : < 
# __le__ : <=
# __gt__ : >
# __ge__ : >=

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return f'이름: {self.name}, 점수: {self.score}'
    
    def __eq__(self, other):
        print("__eq__ 호출됨")
        return self.score == other.score
    
    def __ne__(self, other):
        return self.score != other.score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

s1 = Student("이승협", 90)
s2 = Student("이승협", 100)

s1 == s2  # False
print(s1)