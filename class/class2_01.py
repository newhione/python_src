# 상속의 정의
# 상속은 기존 클래스의 속성과 메서드를 새로운 클래스가 물려받는 것
# 상속의 기본 문법
# class 부모클래스:
#     def 부모메서드(self):
#         print("부모 메서드 호출")

# class 자식클래스:
#     def 자식메서드(self):
#         print("자식 메서드 호출")

class Parents:
    def __init__(self, name):
        self.p_name = name
        print("부모생성자")

    def parents_method(self):
        print("부모클래스 메소드")

class Child(Parents):
    def __init__(self,name,age):
        Parents.__init__(self,name)
        print("자식생성자")

    def child_method(self):
        print("자식클래스 메소드")

c = Child('이승협',34)   #Child 클래스 객체 c
c.parents_method()