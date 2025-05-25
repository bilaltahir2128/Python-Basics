set1={1,2,3,4,5,6,7,8}
print(set1)
set1.add(9)
print(set1)

set1=frozenset(set1)
print(type(set1))
set1=set(set1)
print(type(set1))
set1.add(10)
print(set1)