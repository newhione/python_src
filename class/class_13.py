# 파이썬 클래스에서 getter와 setter 사용법

import random
class Person:
    def __init__(self, name, age):
        self._name = name  # 이름은 변경 불가능하게 설정, private 변수로 설정
        self._age = age    # 나이는 변경 가능하게 설정, private 변수로 설정


# @property -> 함수를 변수처럼 사용할 수 있게 해주는 파이썬의 내장 데코레이터
# @변수명.setter -> 변수를 설정하는 setter 메서드 정의
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            print("나이는 음수가 될 수 없습니다.")


a = Person("이승협", 34)

print(a.age) #34

a.age = 35
print(a.age) #35

a.age = -5 #나이는 음수가 될 수 없습니다.
print(a.age) #35