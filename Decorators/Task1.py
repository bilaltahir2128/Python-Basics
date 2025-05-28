def Decorator(func):
    def wrapper(n):
        if type (n) == int and n >= 0:
            return func(n)
        else:
            raise Exception("Invalid input.")
    return wrapper

                  
        

