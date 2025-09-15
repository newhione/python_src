#가변 매개변수
    # 함수를 정의할 때, 매개변수의 개수를 지정하지 않는다.
    # 함수 내부에서는 리스트로 간주
    # 함수를 호출하는 쪽에서는 편안하게... 1,2,3,4 or 1,2,3,4,5,2,1,3

def myFunc1(args):
    for i in args:
        pass    

# myFunc1(10,20,50,60)  -->  TypeError: myFunc1() takes 1 positional argument but 4 were given
data = [10,20,50,60]
myFunc1(data)


#2.
def myFunc2(*args): # Packing
    for i in args:
        pass

myFunc2(10,20,50,60)  # --> *args(가변 매개변수)를 통해 list로 받을 수 있음

#3.
def myFunc3(args):
    for i in args:
        print(i)

myFunc3([10,20,50,60])

# Unpacking
a,b = [10,20]
print(f'a={a}')
print(f'b={b}')
# 패킹은 