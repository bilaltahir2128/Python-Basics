def Decorator(func):
    def wrapper(n):
        if type (n) == int and n >= 0:
            return func(n)
        else:
            raise Exception("Invalid input.")
    return wrapper

                  
        

@Decorator
def factorial(num):
    if num in (0,1):
        return 1
    else :
        return num*factorial(num-1)
 
no=int(input("Enter a number: "))
print(factorial(no))

    