class parent:

    def par_money(self):
        self.money = 1000
        print("parent money is "+str(self.money))


    def par_property(self):
        self.property = 30
        print("parent property is "+str(self.property))

class child:
    def child_money(self):
        self.money = 2000
        print("child money is "+str(self.money))


    def child_property(self):
        self.property = 40
        print("child property is "+str(self.property))
        
        
class grandchild(parent,child):
    def grandchild_money(self):
        self.money = 2000
        print("grandchild money is " + str(self.money))

    def grandchild_property(self):
        self.property = 40
        print("grandchild property is " + str(self.property))


grandchild = grandchild()
grandchild.child_money()
grandchild.child_property()
grandchild.par_money()
grandchild.par_property()
grandchild.grandchild_money()
grandchild.grandchild_property()
