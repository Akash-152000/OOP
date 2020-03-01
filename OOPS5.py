class student:

    def __init__(self,name,roll,age):
        self.name = name
        self.roll  = roll
        self.age = age
        self.lap = self.laptop()

    def show(self):
        return print(self.name,self.roll,self.age)
        self.lap.show()



    class laptop:

        def __init__(self,):
            self.brand = "Dell"
            self.ram = "8gb"
            self.graphic  = "4gb"

        def show(self):
            return print(self.brand,self.ram,self,graphic)


s1 = student("Akash",74,20)

s1.show()
