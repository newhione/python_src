def change(obj):
    obj[0] = 100

data = [1,2,3]
change(data)
print(data)

# -------------

a=10
b=a
b=1000
print(f'a={a}, b={b}') # a=10, b=1000

list_a = [1,2,3]
# list_b=list_a
list_b=list_a.copy()
list_b[0]=100
print(list_a, list_b) # [100, 2, 3] [100, 2, 3] --> solution: .copy() --> tuple !!
print(list_a, list_b) # [1, 2, 3] [100, 2, 3]
