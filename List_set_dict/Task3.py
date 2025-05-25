integer = [1, -1, 2, -2, 3, -3,4,-4,5,-5,6,-6,7,-7]
sq={}
sq=set(sq)
for i in integer:
    sq.add(i*i)

print(sq)