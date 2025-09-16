# 다형성
# 직원 Employee - 아이디, 이름, 기본급
# 정규직 FullTimeEmployee - 보너스
# 계약직 PartTimeEmployee - 시간당 급여
# 인턴 Intern - 고정수당

class Employee:
    def __init__(self, id, name, base_salary):
        self.id = id
        self.name = name
        self._base_salary = base_salary      #private 의미로 사용
    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salary(self, money):
        if money > 0:
            self._base.salary = money
        else:
            raise ValueError('금액은 양수입니다.')
    
    def show_class(self):
        print('직원 클래스')

    def __str__(self):
        return f'{self.id} : {self.name}, {self.base_salary}'

class FullTimeEmployee(Employee):
    def __init__(self, id, name, base_salary, bonus):
        super().__init__(id, name, base_salary)
        self.bonus = bonus

    def show_class(self):
        print('정규직 클래스')
    
    def __str__(self):
        return super().__str__() + f', {self.bonus}'

class PartTimeEmployee(Employee):
    def __init__(self, id, name, hourly_rate, hours):
        super().__init__(id, name, 0)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def show_class(self):
        print('계약직 클래스') 

    #hourly_rate  hours: getter setter
    def __str__(self):
        return f'{self.id} {self.name} {self.hourly_rate} {self.hours}'
        

class Intern(Employee):
    def __init__(self, id, name, fixed_salary):
        super().__init__(id, name, 0)
        self.fixed_salary = fixed_salary

    def show_class(self):
        print('인턴 클래스')

    def __str__(self):
        return f'{self.id} {self.name} {self.fixed_salary}'
    

# 정규직 직원, 계약직, 인턴을 모두 리스트에 섞어서 객체를 저장
emp = [
    FullTimeEmployee(3872, '이승협', 7000000, 1000000),
    PartTimeEmployee(9098, '유회승', 25000, 8),
    Intern(7042, '서동성', 2300000)
]


for e in emp:
    e.show_class()   #emp 리스트의 각각 개체에 해당하는 메소드를 호출 --> 다형성


