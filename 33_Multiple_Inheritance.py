class Mario():

    def move(self):
        print "I am Moving"

class Shroom():

    def eat_shroom(self):
        print "I am Big"


class BigMario(Mario,Shroom):

    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
