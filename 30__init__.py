"""The __init__ function is called a constructor, or initializer, and is automatically called 
when you create a new instance of a class. Within that function, the newly created object is 
assigned to the parameter self ."""

#Example One
class Tuna:
    def __init__(self):
        print "Hello World"
    def swim(self):
        print "I am Swimming"

flipper = Tuna()
flipper.swim()



#Example Two

class Enemy:
    def __init__(self,x):
        self.energy = x
    def get_energy(self):
        print self.energy

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()
