class Fibnocci:
    def __init__(self,limit):
        self.pervious=0
        self.current=1
        self.n=1
        self.limit=limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n<self.limit:

            result=self.pervious+self.current
            self.pervious=self.current
            self.current=result
            self.n+=1
            return result
        else:
            raise StopIteration
    
fib_iterator = iter(Fibnocci(5))
while True:
    
    try:
        print(next(fib_iterator))
    except StopIteration:
        break