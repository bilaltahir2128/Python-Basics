def factorial(num):
    if num in (0,1):
        return 1
    else :
        return num*factorial(num-1)
 
no=int(input("Enter a number: "))
print(factorial(no))