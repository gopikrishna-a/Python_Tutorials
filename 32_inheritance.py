class Parent():

    def print_last_name(self):
        print "Roberts"

class Child(Parent):
    
    def print_first_name(self):
        print "Bucky"
        
    #Over Writing
    def print_last_name(self):
        print "snitzleberg"
        

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

