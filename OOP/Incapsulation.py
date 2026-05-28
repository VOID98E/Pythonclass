"""

Acess specifier
1.public
2.protected , use single underscore
3.private , use double underscore

"""
# class user:
#     def __init__(self,name,id,password):
#         self.name=name
#         self.id=id
#         self.__password=password #private properties

# a=user("Ram","6767","12345abc")

# print(a.name)
# print(a.__password)


#ACESSING PRIVATE PROPERTIES

# class user:
#     def __init__(self,name,id,password):
#         self.name=name
#         self.id=id
#         self.__password=password #making private properties

#     def get_password(self):
#          return self.__password

#     def set_password(self,password):
#         self.__password=password
        

# a=user("Ram","6767","12345abc")

# a.set_password("shyam123")
# print(a.get_password())

class user:
    def __init__(self,name,password):
        self._name=name
        self._password=password

class student(user):
    def show(self):
        print(self._name)

c=student("ram","ram123")
c.show()

print(c._name)