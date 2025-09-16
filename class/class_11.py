# ininstance() 함수
# 객체가 특정 클래스의 인스턴스(객체)인지 확인하는 데 사용한다.
# 사용하는 이유
# 1. 타입 확인: 함수나 메서드가 특정 클래스의 인스턴스를 기대할 떄, 입력된 객체가 올바른 타입인지 확인하기 위해 사용
# 2. 다형성 지원: 다형성을 활용하는 코드에서, 객체가 특정 클래스의 인스턴스인지 확인하여 적절한 처리
# 3. 오류 방지: 잘못된 타입의 객체가 전달되는 것을 방지하여, 런타임 오류를 줄이기 위해 사용

class Student:
    def study(self):
        return "공부를 합니다."

class Teacher:
    def teach(self):
        return "가르치는 중입니다."

# 리스트에 어떤 객체가 있는지 모를 때 특정 인스턴스만 기대할 수 없다.
# 이럴 때 isinstance() 함수를 사용하여 특정 클래스의 인스턴스인지 확인
peoples = [Student(), Teacher(), Student()]

if isinstance(peoples[0], Student):
    print(peoples[0].study())  # "공부를 합니다." 출력
else:
    print(peoples[0].teach())  
