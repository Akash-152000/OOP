class computer:

    def __init__(self):
        self.name="Computer1"
        self.ram="16gb"

    def config(self):
        print("Configurations are compared")

    def compare(self,other):
        if self.name==other.name:
            return True
        else:
            return False


com1=computer()
com1.name="computer11"
com2=computer()
com2.name="computer22"

if com1.compare(com2):
    print("They are same")
else:
    print("They are different")

com1.config()