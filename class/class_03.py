# __init__ 메서드 --> 생성자, 객체가 만들어질 때 자동으로 실행

class People:
    def __init__(self):
        self.name = None
        self.age = None
        self.addr = None
        print('생성자 호출')

print('h1 객체 생성 전')
h1 = People()
print('h1 객체 생성 후')
print(h1.addr)

# h1 = People()
    # People()을 실행하면 객체가 하나 생성됨.
    # 이 시점에 __init__이 자동으로 호출됩니다.
    # 따라서 self.name, self.age, self.addr라는 인스턴스 변수가 만들어지고 모두 None으로 초기화됩니다.
    # 동시에 print('생성자 호출')이 실행되어 출력됩니다.

class Product: # 클래스 변수 (모든 객체가 공유)
    serial_num = 0

    def __init__(self):
        Product.serial_num += 1 # 클래스 변수 증가
        self.serial_num = Product.serial_num # 인스턴스 변수에 저장
        self.name = None

try1 = Product()
try2 = Product()
try3 = Product()

print(Product.serial_num)  # 3 (클래스 변수, 최종값)
print(try1.serial_num)     # 1 (인스턴스 변수)
print(try2.serial_num)     # 2 (인스턴스 변수)
print(try3.serial_num)     # 3 (인스턴스 변수)
