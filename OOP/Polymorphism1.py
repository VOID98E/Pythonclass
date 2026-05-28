"""
Polymorphism: Single interface, but many implementation

types=1.overriding
      2.overrloading
      3.duck polymorphsim

"""

class animal:
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dog barks")

# a=animal()
# a.sound()

D=dog()
D.sound()