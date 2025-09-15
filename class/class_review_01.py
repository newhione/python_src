# 기본 클래스 생성
class Review:
    # 클래스 변수 생성
    count = 0
    # 생성자 메소드
    def __init__(self, num=0, name=""):
        self.num = num
        self.name = name
        

# 인스턴스 생성(=객체 생성)
r1 = Review(100, '홍길동')
r2 = Review()

# 인스턴스 변수 변경
r1.name = "첫번째 리뷰"

print(f'r1 인스턴스 변수: {r1.name} / r2 인스턴스 변수: {r2.name}') # 인스턴스 변수 접근방법
print(f'클래스 변수: {Review.count}/ r1 클래스 변수: {r1.count}') # 클래스 변수 접근방법: 클래스 변수는 항상 클래스 이름으로 접근하라