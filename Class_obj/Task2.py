class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(f"ID : {self.id} , Name : {self.name} .")

emp=Employee(1,"Failure")
emp.display()

del emp.id

try:
    print(emp.id)
except AttributeError:
    print("emp.id is not defined.")

del emp

try:
    print(emp)
except NameError:
    print("Emp is not defined.")
