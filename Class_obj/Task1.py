class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(f"ID : {self.id} , Name : {self.name} .")

emp=Employee(1,"Failure")
emp.display()


