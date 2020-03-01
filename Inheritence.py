class parent:

    def par_money(self):
        self.money = 1000
        print("parent money is "+str(self.money))


    def par_property(self):
        self.property = 30
        print("parent property is "+str(self.property))

class child(parent):
    def child_money(self):
        self.money = 2000
        print("child money is "+str(self.money))


    def child_property(self):
        self.property = 40
        print("child property is "+str(self.property))

child = child()
child.child_money()
child.child_property()
child.par_money()
child.par_property()