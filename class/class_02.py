# 메소드: 클래스가 갖고 있는 함수
# class 클래스 이름:
    # def 메소드 이름(self, 추가적인 매개변수)
        # pass

class People:
    def make_instance(self):
        self.name = None
        self.age = None
        self.addr = None

h1 = People()
h1.make_instance()
print(h1.addr)
h2 = People()
print(h2.addr)