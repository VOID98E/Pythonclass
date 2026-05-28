"""

OOP=OBJECT ORIENTED PROGRAMMING

1.clean and clear structure
2.reuse of code
3.easy to maintain, easy to debug

class: blueprint, it us collection objects,methods and similar kind of data
syntac = class ClassName
we cannot acess class properties,methods directly so we need objevt for that

object= InSTANCE of a class. it is used to acess and manipulate properties, logic,methods etc of class
syntax= obj=ClassName

charcahteristic of OOp

1.inheritance = to implement the properties of parent class to it child class
2.Polymorphism = single interface, but many implementation
3.incapsulation = BINDING of data and methods, protects data from direct access
4.abstractiond= show only imp details and hiding complex logic or implementation
5.reusability = created once, now we can reuse across the multiple module
6.Message passing = parametres, object


"""
# class Show:
#     name="ram"

#     def show_details(self):
#         print("I am from show_details")
#         return


# stu=Show()#Object
# print(stu.name)
# print(stu.show_details())


# _init_() == constructor

# class Student:

#     name="hari"
#     age="13"

#     def _init_(self):
#         name="Krishna"
#         age="23"

#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print("i am froms show method")


# stu1=Student("ram","23")
# print(stu1.name)
# print(stu1.age)
# print(stu1.show())

# stu2=Student("SHyam","32")
# print(stu2.name)
# print(stu2.age)
# print(stu2.show())

# stu3=Student("Anubhav","13")
# print(stu3.name)
# print(stu3.age)
# print(stu3.show()

# class properties using manipulatiom
class Student:

    name="Hari"
    age="17"

    def __init__(self,name,age):
        self.name=name
        self.age=name

    def show(self):
        print(f"I am from show method hi,{self.name}")

stu1=Student("ram","23")
print(stu1.name)

stu1.name="shiva"

stu1.contact="9383889230e"
print("\n")
print(stu1.contact)
print("\n")

print(stu1.name)
print(stu1.age)
print(stu1.show())