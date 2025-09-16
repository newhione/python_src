from abc import ABC, abstractmethod

class Parents(ABC):   #추상 클래스
    def make_money(self): #일반 메서드
        raise NotImplementedError
    
    @abstractmethod
    def save_money(self): #추상 메서드
        print("저축") 
    
class Child(Parents):
    def make_money(self):  #부모의 make_money 재정의(override)
        print('장사')
    
    def save_money(self):
        print('투자')


c = Child()       #ABC -> @abstractmethod 반드시 사용?
c.make_money()    #다형성  #자식클래스에서 재정의 안 하면 예외 발생하도록 설계 