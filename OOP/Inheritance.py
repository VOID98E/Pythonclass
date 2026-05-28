class user:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show(self):
        print(f"Hi i am from user, hello {self.name}, my id is {self.id}")




class student(user):
    def fromstudent(self):
        print(f"i am from student, hi {self.name}")

obj=student("ram","stu1")
obj.show()
obj.fromstudent()