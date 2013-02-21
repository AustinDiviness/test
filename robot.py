
class Robot:
    def __init__(self, name = "Fred", color = "silver", contents = None):
        self.name = name

    def talk(self):
        print "Bite my shiny metal ass"

class Bender(Robot):
    def __init__(contents = "Amy's watch"):
        super.__init__("Bender", "silver", contents)

    def smoke(self):
        print "puff puff"

class Bender1(Bender):
    def __init__(contents = "Fry's wallet"):
        super.init("Bender", "gold", contents)

    def talk(self):
        print "Bite my glorious metal ass"


        
