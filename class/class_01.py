# class : 사용자 정의 데이터 타입, 사용자 정의 자료구조
# 클래스 변수 vs. 인스턴스 변수

class StudentMng:
    name = '이승협' # 클래스 변수

# class StudentMng(부모클래스):
#     name = '이승협' 

s1 = StudentMng() # 객체(인스턴스) 생성
s2 = StudentMng()
s3 = StudentMng()

s1.name='유회승' #잘 쓰지 않음! 헷갈려 #s1 전용 인스턴스 변수 생성, 이제 s1.name은 '이승협' -> 유회승'이고, s2.name, s3.name은 여전히 클래스 변수 참조('이승협')
StudentMng.name = '서동성' #이걸로 써라 #클래스 변수 변경(클래스명.변수), 클래스 변수가 '이승협' -> 서동성'으로 바뀜./ s2.name, s3.name도 '서동성'으로 변경
print(s1.name, s2.name, s3.name)

# 클래스 변수는 모든 객체가 참조하는 변수
# but 객체가 변수를 재할당받으면 해당 객체는 더 이상 참조하지 않는다.