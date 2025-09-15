list_a = [1,2,3]
tuple_a = (10,20,30,40)
print(f'type(list_a) = {type(list_a)}') # type(list_a) = <class 'list'>
print(f'type(tuple_a) = {type(tuple_a)}') # type(tuple_a) = <class 'tuple'>

tuple(list_a)
print(tuple(list_a)) # (1, 2, 3)

tuple_a = tuple(list_a)
print(tuple_a) # (1, 2, 3)