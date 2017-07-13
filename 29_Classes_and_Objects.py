class Enemy:
    life = 3
    def attack(self):
        print "Ouch!!"
        self.life -=1
    def checklife(self):
        if self.life <= 0:
            print "I am Dead"
        else:
            print str(self.life) + "Life Left"

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()
