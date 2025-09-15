# 다양한 매개변수
    # 기본 매개변수 defult parameter

#1. 
def myAdd(num1, num2, num3):
    return num1 + num2 + num3

result = myAdd(10,20)
print(f'result = {result}')

#2. 
# def myAdd_2(num1, num2=0, num3): # SyntaxError: parameter without a default follows parameter with a default --> default 매개변수는 항상 마지막에
#     return num1 + num2 + num3

# result = myAdd_2(10)
# print(f'result = {result}')

result1 = myAdd()
result2 = myAdd(1)
result3 = myAdd(1,2)
result4 = myAdd(1,2,3)
print(result1, result2, result3, result4)