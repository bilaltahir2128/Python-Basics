def square():
    i=1
    while True:
        yield i*i
        i+=1

for i in square():
    if i>15:
        break
    print(i)

  

