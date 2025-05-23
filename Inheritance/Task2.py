class Teacher:
    def teacher_action(self):
        print("Teacher can teach.")

class Developer:
    def developer_action(self):
        print("Developer can code.")
class Youtuber:
    def youtuber_action(self):
        print("Youtuber can teach as well as code.")


class Person(Teacher,Developer,Youtuber):
    pass

p1=Person()
p1.teacher_action()
p1.developer_action()
p1.youtuber_action()