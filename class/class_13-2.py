# 파이썬 클래스에서 getter와 setter 사용법

import random
class Person:
    def __init__(self, name, age):
        self._name = name  # 이름은 변경 불가능하게 설정, private 변수로 설정
        self._age = age    # 나이는 변경 가능하게 설정, private 변수로 설정

    @property
    def age(self):
        return self._age
    
p1 = Person("이승협", 34)
# print(p1.age()) #34
print(p1.age) #함수의 메모리 주소 => @property를 사용해서 함수처럼 호출하지 않고, 속성처럼 사용 가능