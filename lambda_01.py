# def add(a,b):
#     return a+b

# def minus(a,b):
#     return a-b

def calc(func, a,b):
    return func(a,b)

# print(calc(add, 1,2))

print(calc(lambda a,b: a+b, 1,2))
print(calc(lambda x,y: x*y, 10,20))  # lambda를 사용하는 이유: 따로 함수를 정의할 필요 없이, 한 로직에서만 쓰고 버릴 수 있음!

